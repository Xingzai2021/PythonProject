from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    '我今天去{place}玩了，你知道这个地方吗？'
)

model = ChatOllama(model='qwen3:4b')

parser = StrOutputParser()

chain = prompt | model | parser | model | parser

res = chain.invoke({'place':'广州'})

print(res)