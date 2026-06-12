from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from langchain_ollama import ChatOllama
import config
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from Vector_Searcher import VectorSearcherService
from File_History_Store import get_history


class RagService(object):
    def __init__(self):
        self.model = ChatOllama(model=config.mode)
        self.VectorSearcher = VectorSearcherService()
        self.prompt = ChatPromptTemplate(
            [
                ('system', '你是一个高情商的女朋友。请根据参考资料{context}和历史消息{history}，用亲切、自然的语气回答用户（你的男朋友）的问题。避免机械式的回答，不要把历史消息也重复发出来，不要发和前文高度重复的文字。'),
                MessagesPlaceholder('history'),
                ('human','{input}')
            ]
        )
        self.chain = self.get_chain()


    def get_chain(self):

        def format_document(docs: list[Document]):
            if not docs:
                return "无相关参考资料"

            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段:{doc.page_content}n文档元数据:{doc.metadata}n\n"
            return formatted_str

        def value1(value):
            print(value['input'])
            return value['input']

        def value2(value):
            dict = {}
            dict['input'] = value['input']['input']
            dict['history'] = value['input']['history']
            dict['context'] = value['context']
            return dict

        VectorSearcher = self.VectorSearcher.getVectorSearcher()
        chain =  {'input': RunnablePassthrough(),'context': RunnableLambda(value1) | VectorSearcher | format_document } | RunnableLambda(value2) |self.prompt | self.model

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key='input',
            history_messages_key='history'
        )

        return conversation_chain

if __name__ == '__main__':
    session_config = {
        'configurable': {
            'session_id': 'user_03'
        }
    }
    res = RagService().chain.invoke({'input':'我的身高是多少？是160cm吗？'},session_config)
    print(res.content)
