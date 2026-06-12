from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma

loader = CSVLoader(
    file_path='../data/data.csv',
    encoding="utf-8"
)

doc = loader.load()

store = Chroma(
    collection_name='test',
    embedding_function=DashScopeEmbeddings(),
    persist_directory='./chroma_db'
)

# store.add_documents(
#     documents=doc,
#     ids=[f'id{i}' for i in range(1,len(doc)+1)]
# )

# store.delete(['id1'])

res = store.similarity_search('天宝',1)
print(res)