from openai import OpenAI
import json

client = OpenAI(
    api_key="",
    base_url="http://localhost:11434/v1"
)

scheme = ['期数','中奖号码','一等奖']

examples = [
    {'content':'2026年第20期，开好红球01 02 03 04 05 06 蓝球 07，一等奖中奖为1注',
     'answer':{
         '期数':'2026020',
         '中奖号码':[1,2,3,4,5,6,7],
         '一等奖':'1注'
     }
},
{'content':'202555期,有3注1等奖,10注2等奖,开号篮球7,中奖红球2,4,5,6,8,9',
     'answer':{
         '期数':'2025055',
         '中奖号码':[2,4,5,6,8,9,7],
         '一等奖':'3注'
     }
}
]

messages = [
    {'role':'system','content':f'你是一个汉语言文学的学生，请对文本抽取{scheme}，如果没有提及的信息则输出没有提及。'}
]

for example in examples:
    messages.append({'role':'user','content':example['content']})
    messages.append({'role': 'assistant', 'content': json.dumps(example['answer'], ensure_ascii=False)})

response = client.chat.completions.create(
    model='qwen3:4b',
    messages=messages + [{'role':'user','content':'根据上面的内容，抽取2025111期,10注2等奖,开号篮球11,中奖红球3、5、7、11、12、18'}]
)

print(response.choices[0].message.content)