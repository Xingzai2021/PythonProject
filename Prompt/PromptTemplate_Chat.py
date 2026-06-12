from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','你是一个生活咨询专家，负责解答用户生活上的问题'),
        MessagesPlaceholder('history'),
    ('human','你知道芳和花园吗')
    ]
)

history = [
        ('human','空腹可以喝牛奶吗？'),
        ('ai','空腹不建议喝牛奶？')
]

prompt_text = prompt.invoke({'history':history}).to_string()

model = ChatOllama(model='qwen3:4b')

res = model.invoke(prompt_text)

print(res.content)