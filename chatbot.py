import streamlit as st
import openai
import os
import json
import random

def chatbot():
        st.title("💬 Chatbot")
        message = st.chat_message("User")
        left_column, right_column = st.columns([3,1])
        with left_column: 
                response = random.choice (
                        [
                                "Hello!", "Hi There!", "Hi!",
                        ]
                )
                message.write(response)
         # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
                
        if prompt := st.chat_input("Message your AI mentor!"):
                # Display user message in chat message container
                st.session_state.messages.append({"role": "user","content": prompt})

        for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                        st.markdown(message["content"])
                st.text_input("I am doing good! How are you?")

