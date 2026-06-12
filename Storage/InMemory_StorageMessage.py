from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

prompt = ChatPromptTemplate(
    [
        ('system','你将根据历史消息回答用户的问题'),
        MessagesPlaceholder('history'),
        ('human','{input}')
    ]
)

model = ChatOllama(model='qwen3:4b')

chain = prompt | model

session_ids = {}
#拿到存储对应sessionID的消息存储器（历史消息）
def get_history(session_id):
    if session_id not in session_ids:
        session_ids[session_id] = InMemoryChatMessageHistory()
    return session_ids[session_id]


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

    res = prompt_with_history.invoke({'input':'我有一只猫'},session_config)
    print(res.content)

    res = prompt_with_history.invoke({'input': '我有两只狗'}, session_config)
    print(res.content)

    res = prompt_with_history.invoke({'input': '我一共有几只宠物？'}, session_config)
    print(res.content)