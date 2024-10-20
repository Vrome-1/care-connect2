import streamlit as st
import random
import time
import os 
import openai
# Set your OpenAI API key from environment variable
def chatbot():
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

        for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                        st.markdown(message["content"])
                        
        if prompt := st.chat_input("Message your AI mentor!"):
                # Display user message in chat message container
                st.session_state.messages.append({"role": "user","content": prompt})


'''st.title("AI Health Mentor")
    st.markdown("Chat with our AI mentor for support and guidance. Your conversations are private and confidential.")

    # Initialize OpenAI client with API key from environment variable
    api_key =  'sk-W2J7u45G4vDH9G90Ab4F88a0OA2gBJvfzjn2qlNftjT3BlbkFJKBEKXSe9UhEYAAjXBtf1AaNbPbNKfih1A088hFrWIA'

    if not api_key:
        st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return

    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        st.error(f"Error initializing OpenAI client: {str(e)}")
        return

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add system message to set the AI's role
        st.session_state.messages.append({
            "role": "system",
            "content": "You are a compassionate health mentor who provides emotional support and guidance to patients. Focus on being empathetic and encouraging while maintaining appropriate boundaries. Do not provide medical advice."
        })

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] != "system":  # Don't display system messages
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            # Get AI response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
               
                # Stream the response
                for response in client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    stream=True
                ):
                    if response.choices[0].delta.content is not None:
                        full_response += response.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
               
                message_placeholder.markdown(full_response)
               
            # Add assistant's response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error generating response: {str(e)}")'''
               
        

'''openai.api_key = st.secrets["sk-W2J7u45G4vDH9G90Ab4F88a0OA2gBJvfzjn2qlNftjT3BlbkFJKBEKXSe9UhEYAAjXBtf1AaNbPbNKfih1A088hFrWIA"]
        #openai.api_key = os.environ.get("sk-W2J7u45G4vDH9G90Ab4F88a0OA2gBJvfzjn2qlNftjT3BlbkFJKBEKXSe9UhEYAAjXBtf1AaNbPbNKfih1A088hFrWIA")
        client = OpenAI(
                api_key = "sk-W2J7u45G4vDH9G90Ab4F88a0OA2gBJvfzjn2qlNftjT3BlbkFJKBEKXSe9UhEYAAjXBtf1AaNbPbNKfih1A088hFrWIA"
        )
                # Display chat messages from history on app rerun
                # Display user message
        
        
                with st.chat_message("assistant"):
                    # Call the OpenAI API to generate a response
                    message_placeholder = st.empty()
                    full_response = ""
                    for response in openai.ChatCompletion.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                            stream=True,
                    ):
                            
        
                    # Extract AI's response
                    ai_response = completion.choices[0].message['content']
        
                    # Display AI response and add it to the session state
                    with st.chat_message("assistant"):
                        st.markdown(ai_response)
        
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                except Exception as e:
                    st.error(f"Error: {e}")'''
