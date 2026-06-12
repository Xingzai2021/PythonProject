from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

prompt = PromptTemplate.from_template(
    '我姓{name}，我生了一个{gender}。请帮我起名字。'
)

# prompt_text = prompt.format(name='罗',gender='女儿')
#
# model = ChatOllama(model='qwen3:4b')
#
# res = model.invoke(input=prompt_text)

model = ChatOllama(model='qwen3:4b')

chain = prompt | model

res = chain.invoke(input={'name':'罗','gender':'女儿'})

print(res.content)