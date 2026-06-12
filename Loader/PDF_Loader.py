from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path='../data/lyx.pdf',
    mode='page',
    password='123456'
)

i=0
for doc in loader.lazy_load():
    i +=1
    print(doc)
    print(i)