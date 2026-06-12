from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="http://localhost:11434/v1"
)

types = ['好的','坏的','不清楚']

examples = {
    '好的':'我今天中彩票了',
    '好的':'我考上研究生了',
    '好的':'我被路人夸长得好看了',
    '坏的':'我今天出门不小心踩到水滩，把鞋子弄湿了',
    '坏的':'我被人骗钱了'
}

messages = [
    {'role':'system','content':'你是一个汉语言文学的学生，请将文本分类成["好的","坏的"]，如果不能分辨则输出我不清楚。'}
]

for key,value in examples.items():
    messages.append({'role':'user','content':value})
    messages.append({'role': 'assistant', 'content': key})

response = client.chat.completions.create(
    model='qwen3:4b',
    messages=messages + [{'role':'user','content':'我是罗远兴'}]
)

print(response.choices[0].message.content)