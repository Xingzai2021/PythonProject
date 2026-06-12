from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

chat_model = ChatOllama(model='qwen3:4b')

messages=[
    SystemMessage(content='你是一个AI开发工程师，同时兼职生活咨询'),
    HumanMessage(content='帮我想一下通勤路上可以做些什么提升自己的事情')
]

messages1=[
    ('system','你是一个AI开发工程师，同时兼职生活咨询'),
    ('human','帮我想一下通勤路上可以做些什么提升自己的事情')
]

res = chat_model.stream(messages1)

for chunk in res:
    print(chunk.content,end='',flush=True)