from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call,wrap_tool_call
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.runtime import Runtime


@before_agent
def before_agent(state:AgentState,runtime:Runtime):
    print(f"before agent, have {len(state['messages'])}")

@after_agent
def after_agent(state:AgentState,runtime:Runtime):
    print(f"after agent, have {len(state['messages'])}")

@before_model
def before_model(state:AgentState,runtime:Runtime):
    print(f"before_model, have {len(state['messages'])}")

@after_model
def after_model(state:AgentState,runtime:Runtime):
    print(f"after_model, have {len(state['messages'])}")

@wrap_model_call
def model_call_hook(request,handler):
    print(f"model action")
    return handler(request)

@wrap_tool_call
def monitor_tool(request,handler):
    print(f"{request.tool_call['name']}")
    print(f"{request.tool_call['args']}")
    return handler(request)

@tool(description='传入需要查询天气的城市名字，返回的是字符串')
def get_weather(city:str)->str:
    return f'{city}天气：暴雨'

model = ChatOllama(model='qwen3:4b')

agent = create_agent(
    model=model,
    tools=[get_weather],
    middleware=[before_agent, after_agent, before_model, after_model, monitor_tool, model_call_hook]
)

res = agent.invoke({
    'messages':[
        {'role':'human','content':'帮我查一下广州应该穿什么样的衣服？'}
    ]
})

print(res)