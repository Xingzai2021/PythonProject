from openai import OpenAI

client = OpenAI(
    api_key="sk-f92f50bfc4fb42bfa8c012de365c153f",
    base_url="http://localhost:11434/v1"
)

response = client.chat.completions.create(
    model="qwen3:4b",
    messages=[
        {'role':'system','content':'我是一个生活常识问答助手，回答问题的风格是很详细'},
        {'role': 'assistant', 'content': '你好，我是生活问答小助手'},
        {'role': 'user', 'content': '我有一只猫'},
        {'role': 'assistant', 'content': '好的，我知道了'},
        {'role': 'user', 'content': '我还有两只猫'},
        {'role': 'assistant', 'content': '好的，我知道了'},
        {'role': 'user', 'content': '我一共有几只猫？'}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content,end=' ',flush=True)