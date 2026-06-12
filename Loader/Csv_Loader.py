from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='../data/data.csv',
    encoding='utf-8',
    csv_args={
        'delimiter': ',', #指定分隔符
        'quotechar': '"', #指定内容包裹符号
        # 'fieldnames':['a','b'] 自定义表头（若已有表头就不要使用）
    }
)

# document = loader.load()
# print(document)

for document in loader.lazy_load(): #懒加载，适用于数据集非常庞大时
    print(document)