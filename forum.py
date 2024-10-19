import streamlit as st

# Placeholder for user stories
user_stories = []

# Page selection for Community Forum
    st.title('Our Care Community Forum :heart:')
    st.subheader("Today's Posts")
    
    # Display existing stories
    for story in user_stories:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <img src="{story['profile_pic']}" style="border-radius: 50%; width: 50px; height: 50px; margin-right: 10px;">
                <div>
                    <strong>{story['name']}</strong><br>
                    {story['title']}<br>
                    {story['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # Input for new user story
    st.subheader("Share Your Story")
    name = st.text_input("Your Name")
    title = st.text_input("Title of Your Story")
    content = st.text_area("Write your story here...")
    profile_pic_url = st.text_input("Profile Picture URL")  # Allow users to add their own profile picture

    # Button to submit the story
    if st.button("Submit"):
        if name and title and content and profile_pic_url:
            # Add the new story to the user_stories list
            user_stories.append({
                'name': name,
                'title': title,
                'content': content,
                'profile_pic': profile_pic_url
            })
            st.success("Your story has been added!")
        else:
            st.error("Please fill in all fields.")

st.title('Our Care Community Forum :heart:');
    st.subheader("Today's Posts");
    st.success("Preeti Patel  \nMy story  \n Hi guys, I'm a new Care Connect user and I wanted to share my story today. I've been struggling with my mental health for over a year now, just shortly after my diagnosis of breast cancer. I'm fortunate enough to have a very loving family, but even still I feel alone because they don't know what it's like to go through this. I also feel guilty for not being able to be as strong of a mom as I used to be. Does it ever get better?");
    st.write("---> Sending lots of love from a breast cancer survivor. I get you girl, and I know it's hard, but we will prevail. Tip for you: keep a positive thoughts journal to help you combat those negative feelings.");
