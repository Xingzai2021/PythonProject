import streamlit as st
from RAG import RagService
import config

st.title('🤖 AI伴侣')
st.divider()

if "message" not in st.session_state:#创建message的key并且存入欢迎语
    st.session_state["message"] = [{"role": "assistant", "content": "今天心情怎么样? "}]
if "rag" not in st.session_state:#创建一个全生命周期的RAG服务实例类
    st.session_state["rag"] = RagService()
for message in st.session_state["message"]:#将所有历史消息输出
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    st.chat_message('user').write(prompt)
    st.session_state['message'].append({'role':'user','content':prompt})

    ai_res = []
    with st.spinner('思考中...'):
        res_stream = st.session_state['rag'].chain.stream({'input':prompt},config.session_config)

        def capture(generator,cache):
            for chunk in generator:
                cache.append(chunk.content)
                yield chunk

        st.chat_message('assistant').write_stream(capture(res_stream,ai_res))
        st.session_state['message'].append({'role':'assistant','content':''.join(ai_res)})

































