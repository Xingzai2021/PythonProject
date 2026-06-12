from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    file_path='../data/data.txt',
    encoding='utf-8',
)

doc = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=['/n/n','/n','！','!','?','.','？','.','',' '],
    length_function=len
)

docs = splitter.split_documents(doc)
print(len(docs))
for doc in docs:
    print('='*20)
    print(doc)
    print('=' * 20)
