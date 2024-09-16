
import streamlit as st
from chat import init_cs_bot_session
st.title("AI Omega CS")

if 'chat_bot' not in st.session_state:
    st.session_state['chat_bot'] = init_cs_bot_session()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Omega CS!"}
    ]
if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Hi Omega"):
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response =st.session_state['chat_bot'].send_message(prompt).candidates[0].content.parts[0].text.strip()
    st.session_state["response"] = response
    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": st.session_state["response"]})
        st.write(st.session_state["response"])
        
