from langchain_ollama import OllamaLLM

llm = OllamaLLM(model='qwen3:4b')

res = llm.stream('你是什么模型，说出你的模型代号')

for chunk in res:
    print(chunk,end='',flush=True)
