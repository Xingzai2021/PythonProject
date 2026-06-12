from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

model = ChatOllama(model='qwen3:4b')

@tool(description='获取食物名称')
def get_name():
    return '三文鱼'

@tool(description='获取食物价格')
def get_price():
    return 80

agent = create_agent(
    model=model,
    tools=[get_price,get_name],
    system_prompt = '你是严格遵循ReAct框架的智能体，必须按「思考一行动一观察一再思考」的流程解决问题.且**每轮仅能思考并调用1个工具**，禁止单次调用多个工具。并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我'
)

for chunk in agent.stream(
    input={'messages':[
        {'role':'user','content':'帮我查一下食物的名字和价格'}
    ]},
    stream_mode='values'
):
    if chunk['messages'][-1].content:
        print(chunk['messages'][-1].content)
    try:
        if chunk['messages'][-1].tool_calls:
            for tool_call in chunk['messages'][-1].tool_calls:
                print(tool_call['name'])
    except:
        pass