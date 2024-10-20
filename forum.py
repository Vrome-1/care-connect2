import streamlit as st

# Function to display the community forum
def forum():
    # Initialize user stories in session state if not already done
    if 'user_stories' not in st.session_state:
        st.session_state.user_stories = [
            {'name': 'Preeti Patel', 'title': 'My Journey', 'content': "Hi guys, I'm a new Care Connect user and I wanted to share my story today. I've been struggling with my mental health for over a year now, just shortly after my diagnosis of breast cancer."},
            {'name': 'Elaine G', 'title': 'Daily Update', 'content': "Good day all. As usual, my daily update. My doctor changed my meds, and now I feel nauseous all the time. Guess it's better than the other ones though because they affect my mood less. I'm really addicted to Words With Friends right now, effectively gets my mind off everything. Anyone want to play with me sometime?"}
        ]

    st.title('Our Care Community Forum :heart:')
    st.subheader("Today's Posts")

    # Displaying user stories
    if st.session_state.user_stories:
        for story in st.session_state.user_stories:
            st.markdown(f"""
            <div style="background-color:rgba(255, 105, 180, 0.2); padding:10px; border-radius:5px; color:black; margin-bottom:20px;">
                <p style="font-size:24px; font-weight:bold; margin:0;">{story['name']}</p>
                <p style="font-size:20px; margin:0;">{story['title']}</p>
                <p style="margin-top:5px;">{story['content']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.subheader("Share Your Story")

    # Temporary storage for input fields
    if 'temp_name' not in st.session_state:
        st.session_state.temp_name = ""
    if 'temp_title' not in st.session_state:
        st.session_state.temp_title = ""
    if 'temp_content' not in st.session_state:
        st.session_state.temp_content = ""

    # Input fields
    st.session_state.temp_name = st.text_input("Your Name", st.session_state.temp_name)
    st.session_state.temp_title = st.text_input("Title of Your Story", st.session_state.temp_title)
    st.session_state.temp_content = st.text_area("Write your story here...", st.session_state.temp_content)

    # Button to submit the story
    submit_clicked = st.button("Submit")
    if submit_clicked:
        if st.session_state.temp_name and st.session_state.temp_title and st.session_state.temp_content:
            # Add the new story to the user_stories list in session state
            st.session_state.user_stories.append({
                'name': st.session_state.temp_name,
                'title': st.session_state.temp_title,
                'content': st.session_state.temp_content,
            })
            st.success("Your story has been added!")  # Confirm submission
            
            # Clear the temporary input fields
            st.session_state.temp_name = ""
            st.session_state.temp_title = ""
            st.session_state.temp_content = ""
            # Rerun the app to refresh
            
        else:
            st.error("Please fill in all fields.")

# Call the forum function
forum()

