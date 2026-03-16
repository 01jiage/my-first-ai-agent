import streamlit as st
import anthropic

# 设置页面
st.title("🤖 智能助手")

# 初始化对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史对话
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 用户输入框
user_input = st.chat_input("输入你的问题...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    client = anthropic.Anthropic(api_key="sk-qslMXny0o4vnbTAquW3PuHooyDsFtnRza8Z3ME3RmweaVA3E")  # 换成你的key
    
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=st.session_state.messages
            )
        answer = response.content[0].text
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})