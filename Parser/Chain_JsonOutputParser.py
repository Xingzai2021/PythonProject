from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from langchain_core.runnables import RunnableLambda

prompt1 = PromptTemplate.from_template('我的名字叫做{name1}，请帮我的女儿起名字，你只需要返回一个名字就可以')
prompt2 = PromptTemplate.from_template('{name2}，请帮我解析这个名字的含义')

model = ChatOllama(model='qwen3:4b')

json_parser = JsonOutputParser()
string_parser = StrOutputParser()
#自定义类型转换函数(RunnableLambda()可以去除，langchain可接受callable函数)
my_parser = RunnableLambda(lambda AiMessage : AiMessage.content)

chain = prompt1 | model | my_parser | prompt2 | model | string_parser

for chunk in chain.stream({'name1':'罗远兴'}):
    print(chunk,end='',flush=True)