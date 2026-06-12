from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_ollama import ChatOllama

example_prompt = PromptTemplate.from_template('单词:{word},反义词:{antonym}')

examples = [
    {'word':'大','antonym':'小'},
    {'word':'上','antonym':'下'}
]

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    prefix='告诉我单词的反义词，如下面的提示：',
    suffix='基于前面的示例，请你告诉我{input_word}的反义词，简短一些。',
    input_variables=['input_word']
)

model = ChatOllama(model='qwen3:4b')

prompt_text = prompt.invoke(input={'input_word':'有钱'})

res = model.invoke(prompt_text)

print(res.content)