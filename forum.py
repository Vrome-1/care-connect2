import streamlit as st

# Function to display the community forum
def forum():
    # Initialize user stories in session state if not already done
     
    if 'user_stories' not in st.session_state:
        st.session_state.user_stories = []

    st.title('Our Care Community Forum :heart:')
    st.subheader("Today's Posts")

    # Sample posts
    st.success(
        "Preeti Patel  \nHi guys, I'm a new Care Connect user and I wanted to share my story today. "
        "I've been struggling with my mental health for over a year now, just shortly after my diagnosis of breast cancer. "
        "I'm fortunate enough to have a very loving family, but even still I feel alone because they don't know what it's like to go through this. "
        "I also feel guilty for not being able to be as strong of a mom as I used to be. Does it ever get better?"
    )
    
    st.success(
        "Elaine G.  \nGood day all. As usual, my daily update. My doctor changed my meds, and now I feel nauseous all the time. "
        "Guess it's better than the other ones though because they affect my mood less. I'm really addicted to Words With Friends right now, "
        "effectively gets my mind off everything. Anyone want to play with me sometime?"
    )

    # Display all user stories, including new submissions
    if st.session_state.user_stories:
        st.subheader("User Stories")
        for story in st.session_state.user_stories:
            st.success(f"{story['name']}  \n{story['title']}  \n{story['content']}")  # Display in the same format

    st.subheader("Share Your Story")
    name = st.text_input("Your Name")
    title = st.text_input("Title of Your Story")
    content = st.text_area("Write your story here...")
    
    # Button to submit the story
    if st.button("Submit"):
        if name and title and content:
            # Add the new story to the user_stories list in session state
            st.session_state.user_stories.append({
                'name': name,
                'title': title,
                'content': content,
            })
            st.success("Your story has been added!")  # Confirm submission
        else:
            st.error("Please fill in all fields.")


