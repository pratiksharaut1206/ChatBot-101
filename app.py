import streamlit as st
from llm import get_response  ## function to connect with an LLM and get the ouput

st.title("Chat with your ChatGPT assistant")

## we are creating a message history using session_state
if "messages" not in st.session_state:
    st.session_state.messages = []   ## session_state is a temp database for every user session

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

## Capture user input and store in variable user_input
user_input = st.chat_input("Type your message...")

## Store the message in memory and display the input 
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = get_response(st.session_state.messages)
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})