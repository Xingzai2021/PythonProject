from langchain_community.document_loaders import JSONLoader


loader = JSONLoader(
    file_path='../data/data.json',
    jq_schema='.', #jq数据抽取语法
    text_content=False, #抽取的是否字符串
    json_lines=True #抽取的格式是不是多行json格式（非标准json格式）
)

document = loader.load()
print(document)