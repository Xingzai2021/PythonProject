import hashlib,os,config
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings

def check_md5(string):
    if not os.path.exists(config.md5_path):
        with open(config.md5_path, 'w',encoding='utf-8') as f:
            pass
        return False
    with open(config.md5_path, 'r',encoding='utf-8') as f:
        for line in f.readlines():
            if line.strip() == string:
                return True
    return False

def save_md5(string):
    with open(config.md5_path, 'a',encoding='utf-8') as f:
        f.write(string+'\n')

def str_to_md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

class knowledgeBaseService(object):
    def __init__(self):
        self.chroma = Chroma(
    collection_name=config.collection_name,
    embedding_function=DashScopeEmbeddings(),
    persist_directory=config.persist_directory
)
        self.spliter = RecursiveCharacterTextSplitter(
    chunk_size=config.chunk_size,
    chunk_overlap=config.chunk_overlap,
    separators=config.separators,
    length_function=config.length_function
)

    def str_vector_uploader(self, string, filename):
        md5 = str_to_md5(string)
        if check_md5(md5):
            return '[失败]该向量已经存在！'
        else:
            if len(string) > config.need_to_split:
                string_chunk = self.spliter.split_text(string)
            else:
                string_chunk = [string]
            self.chroma.add_texts(string_chunk, metadatas=None, filename=filename)
            save_md5(md5)
            return '[成功]已成功存入向量库！'


if __name__ == '__main__':
    service = knowledgeBaseService()
    res = service.str_vector_uploader('兴仔2','name')
    print(res)