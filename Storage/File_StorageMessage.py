import os,json
from collections.abc import Sequence
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_ollama import ChatOllama

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path

        self.file_path = os.path.join(self.storage_path,self.session_id) #连接得到完整的存储路径
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True) #确保路径文件存在，不存在则新建

    def add_messages(self,messages:Sequence[BaseMessage]) -> None:
        history_messages = list(self.messages) #历史消息作为父类的成员变量以消息类格式存储，要先转化成Sequence才能和Sequence相加
        history_messages.extend(messages)

        json_history_messages = [message_to_dict(message) for message in history_messages] #将所有message类序列化，便于阅读
        with open(self.file_path,'w',encoding='utf-8') as f:
            json.dump(json_history_messages,f)

    @property #messages在父类中必须以成员变量存在
    def messages(self) -> list[BaseMessage]:
        if not os.path.exists(self.file_path): #如果是第一次运行，没有历史消息，则返回空列表
            return []
        with open(self.file_path,'r',encoding='utf-8') as f:
            return messages_from_dict(json.load(f)) #把序列化格式转回message格式

    def clear(self) -> None:
        with open(self.file_path,'w',encoding='utf-8') as f:
            json.dump([],f) #清空方式：写空列表


from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

prompt = ChatPromptTemplate(
    [
        ('system','你将根据历史消息回答用户的问题'),
        MessagesPlaceholder('history'),
        ('human','{input}')
    ]
)

model = ChatOllama(model='qwen3:4b')

chain = prompt | model

#拿到存储对应sessionID的消息存储器（历史消息）
def get_history(session_id):
    return FileChatMessageHistory(session_id=session_id, storage_path='../history')


prompt_with_history = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key='input',
    history_messages_key='history'
)

if __name__ == '__main__':
    session_config = {
        'configurable': {
            'session_id': 'user_01'
        }
    }

    # res = prompt_with_history.invoke({'input':'我有一只猫'},config=session_config)
    # print(res.content)
    #
    # res = prompt_with_history.invoke({'input': '我有两只狗'}, config=session_config)
    # print(res.content)

    res = prompt_with_history.invoke({'input': '我一共有几只宠物？'}, config=session_config)
    print(res.content)

