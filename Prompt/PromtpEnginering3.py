from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="http://localhost:11434/v1"
)

examples = {
    '有关系':[('今天下雨','我不出门'),('今天星期六','我休息')],
    '没关系':[('今天下雨','我洗澡'),('今天星期六','我想吃饭')]
}

messages = [
    {'role':'system','content':'你是一个汉语言文学的学生，请帮我完成文本匹配，用括号括住并用逗号隔开了前后两句话，返回"有关系"或者"没关系"。'}
]

for key,value in examples.items():
    messages.append({'role':'user','content':f'句子1：{value[0]}，句子2：{value[1]}'})
    messages.append({'role': 'assistant', 'content': key})

response = client.chat.completions.create(
    model='qwen3:4b',
    messages=messages + [{'role':'user','content':'(我是男的，我获得工资)'}]
)

print(response.choices[0].message.content)