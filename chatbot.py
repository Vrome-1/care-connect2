import streamlit as st
import openai
import os
import json

def chatbot():
         # Show title and description
         st.title("💬 Chatbot")
         st.write(
         "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
             "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
         )
    
         #Configuring openai - api key
         working_dir = os.path.dirname(os.path.abspath(__file__))
         config_data = json.load(open(f"(working_dir)/config.json"))
         OPEN_API_KEY = config_data["sk-W2J7u45G4vDH9G90Ab4F88a0OA2gBJvfzjn2qlNftjT3BlbkFJKBEKXSe9UhEYAAjXBtf1AaNbPbNKfih1A088hFrWIA"]
         openai.api_key = OPEN_API_KEY

        # Create a session state variable to store the chat messages
         if "messages" not in st.session_state:
             st.session_state.messages = []

        # Display the existing chat messages
         for message in st.session_state.messages:
             with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input for the user
         if prompt := st.chat_input("What is up?"):
            # Store and display the user's prompt
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate a response using the OpenAI API
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
         )

         # Extract the assistant's message and store it in session state
         assistant_message = response['choices'][0]['message']['content']
         st.session_state.messages.append({"role": "assistant", "content": assistant_message})
            
         # Display the assistant's response
         with st.chat_message("assistant"):
                st.markdown(assistant_message)
