md5_path = './md5.txt'
collection_name = 'vector'
persist_directory = './vector_db'
chunk_size=1000
chunk_overlap=50
separators=['/n/n','/n','！','!','?','.','？','.','',' ']
length_function=len
need_to_split=10
similarity_threshold=2
mode = 'qwen3:4b'
session_config = {
        'configurable': {
            'session_id': 'user_03'
        }
    }