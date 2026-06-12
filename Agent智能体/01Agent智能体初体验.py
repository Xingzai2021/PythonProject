from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

@tool(description='查询天气')
def get_weather():
    return '多云'

agent = create_agent(
    model=ChatOllama(model='qwen3:4b'),
    tools=[get_weather],
    system_prompt='请根据用户提问，回答问题'
)

prompt = {
    'messages':[
        {
        'role':'human','content':'请帮我查询明天的天气'
        }
    ]
}

res = agent.invoke(prompt)

for msg in res['messages']:
    print(type(msg).__name__,'：',msg.content)