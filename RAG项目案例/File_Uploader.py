import streamlit as st
from KnowledgeBase import knowledgeBaseService

st.title('知识库更新服务')

uploader = st.file_uploader(
    label='请上传【txt】文件',
    type='txt',
    accept_multiple_files=False,
)

if 'service' not in st.session_state:
    st.session_state['service'] = knowledgeBaseService()

if uploader:
    st.subheader(f'文件名：{uploader.name}')
    st.write(f'类型：{uploader.type} | 大小：{round(uploader.size/1024,2)}KB')

    text = uploader.getvalue().decode('utf-8')

    with st.spinner('知识库载入中...'):
        res = st.session_state['service'].str_vector_uploader(text, uploader.name)
        st.write(res)

