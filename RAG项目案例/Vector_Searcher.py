from langchain_chroma import Chroma
import config
from langchain_community.embeddings import DashScopeEmbeddings

class VectorSearcherService(object):
    def __init__(self):
        self.embeddings = DashScopeEmbeddings()
        self.chroma = Chroma(
    collection_name=config.collection_name,
    embedding_function=DashScopeEmbeddings(),
    persist_directory=config.persist_directory
)

    def getVectorSearcher(self):
        return self.chroma.as_retriever(search_kwargs={'k':config.similarity_threshold})

if __name__ == '__main__':
    vectorSearcher = VectorSearcherService()
    res = vectorSearcher.getVectorSearcher().invoke('你好')
    print(res)