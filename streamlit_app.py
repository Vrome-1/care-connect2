import streamlit as st
from openai import OpenAI
from forum import forum
from chatbot import chatbot
from buddy import buddy
st.set_page_config(
    page_title="Connect Care",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state = "auto",
)

st.markdown(
    """
    <div style='background-color: #f0f2f5; padding: 20px; border-radius: 10px; text-align: center;'>
        <h1 style='margin: 0; color: #333;'>Connect Care 🤝</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Increase the font size of sidebar items */
    .sidebar .sidebar-content {
        font-size: 35px;  /* Change this value for desired font size */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("Navigation\n____")
page = st.sidebar.radio("Choose a page", ["About", "Educational Resources", "Community Forum", "Chatbot", "Health Buddy"])

if page == "About":
    st.header("About Connect Care");
    st.markdown("<p style='font-size:20px;'>Welcome to Care Connect! This website is all about support and community - we aim to help patients find and connect with others who understand what they are going through. Connect Care aims to connect patients to their community so that they can find others who understand what they are going through and help them.</p>", unsafe_allow_html=True)
    st.header("Inspiration");
    st.markdown("<p style='font-size:20px;'>We understand that, in healthcare, mental health is key. Patients go through a lot of stress related to their illnesses - both physical and emotional. As college students we have seen how our community can help us get through difficult times. We want patients to be able to feel like they are heard. By conencting with others they will be able to know that others understand their situation and be able to learn from others. We hope that Connect Care will allow patients to get in touch with a unique community that will continue to grow.</p>", unsafe_allow_html=True)
    st.header("Features")
    st.markdown("<p style='font-size:20px;'>We have included a variety of features to help patients with their healthcare: </p>", unsafe_allow_html=True)
    st.subheader("1) The Community Health Forum");
    st.markdown("<p style='font-size:20px;'>This is a way for us to find people who are going through the same things as us. Here, patients can let all their feelings out and find others who can give them support and tips for managing their feelings. Users can post however frequently they want, and it can become a type of journal/blog for those who want to provide daily updates.</p>", unsafe_allow_html=True)
    st.subheader("2) The Chatbot");
    st.markdown("<p style='font-size:20px;'>This is for people who just need to get their feelings out. The Chatbot can provide comforting reassurance, and advice. This is a good alternative to the community forum if users are  shy or are hesitant to share their feelings publicly.</p>", unsafe_allow_html=True)
elif page == "Community Forum":
    forum()
elif page == "Educational Resources":
    st.title("Resources")
    st.write("If you or someone you know is struggling as a patient please use these resources to help: ")
    col1, col2 = st.columns(2)
    with col1:
        st.header("People")
        st.markdown("- local doctor")
        st.markdown("- find a health buddy")
        st.markdown("- attend a local support group")
    with col2:
        st.header("Websites")
        st.markdown("- https://www.ncoa.org/adviser/medical-alert-systems/support-for-older-adults-living-alone/")
        st.markdown("- https://www.cdc.gov/mental-health/about/?CDC_AAref_Val=https://www.cdc.gov/mentalhealth/learn/index.htm")
        st.markdown("- https://www.patientadvocate.org/")
        st.markdown("- https://themighty.com")
        st.markdown("")
        
elif page == "Chatbot":
    chatbot()
elif page == "Health Buddy":
    buddy()

# # Show title and description.
# st.title("💬 Chatbot")
# st.write(
#     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
# )

# # Ask user for their OpenAI API key via `st.text_input`.
# # Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# # via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display the existing chat messages via `st.chat_message`.
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Create a chat input field to allow the user to enter a message. This will display
#     # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

#         # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})
