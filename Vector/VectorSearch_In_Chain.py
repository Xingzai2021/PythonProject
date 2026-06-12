from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import DashScopeEmbeddings

model = ChatOllama(model='qwen3:4b')
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','请根据参考资料{context}回答问题'),
        ('human','{input}')
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())
vector_store.add_texts(['多健身就可以减肥了','饮食规律可以帮助减肥','有些人吃完饭会感到头晕是因为吃碳水会晕碳'])

input = '为什么我吃完饭后会犯困呢？'

#向量检索vector_store.similarity_search()的返回格式变成runnable的子类（入chain）
retriever = vector_store.as_retriever(search_kwargs={'k':2})

def list_to_str(docs) -> str:
    list = [doc.page_content for doc in docs]
    return ','.join(list)

def print_prompt(prompt):
    print(prompt)
    return prompt

chain = {'input':RunnablePassthrough(),'context':retriever | list_to_str} | prompt | print_prompt | model

res = chain.invoke(input)
print(res.content)

