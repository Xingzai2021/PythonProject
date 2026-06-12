from langchain_ollama import ChatOllama
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

model = ChatOllama(model='qwen3:4b')
prompt = ChatPromptTemplate(
    [
        ('system','你将根据参考资料{context}回答用户问题，可以再加一点你自己的理解。'),
        ('human','{input}')
    ]
)

store = InMemoryVectorStore(embedding=DashScopeEmbeddings())
store.add_texts(['打篮球有助于长高','作息规律对身体好','吃饭有助于长身体'])

input = '打篮球对身体有什么好处？'

res = store.similarity_search(input,2)
reference = []
for item in res:
    reference.extend(item)

def prompt_print(prompt):
    print(prompt)
    return prompt

chain = prompt | prompt_print | model

res = chain.invoke({'input':input,'context':reference})
print(res.content)

