import streamlit as st

# Placeholder for user stories
def forum():
    st.title('Our Care Community Forum :heart:');
    st.subheader("Today's Posts");
    st.success("Preeti Patel  \n Hi guys, I'm a new Care Connect user and I wanted to share my story today. I've been struggling with my mental health for over a year now, just shortly after my diagnosis of breast cancer. I'm fortunate enough to have a very loving family, but even still I feel alone because they don't know what it's like to go through this. I also feel guilty for not being able to be as strong of a mom as I used to be. Does it ever get better?");
    st.success("Elaine G.  \n Good day all. As usual, my daily update. My doctor changed my meds, and now I feel nauseous all the time. Guess it's better than the other ones though because they affect my mood less. I'm really addicted to Words With Friends right now, effectively gets my mind off everything. Anyone want to play with me sometime?");
    st.write("---> Sending lots of love from a breast cancer survivor. I get you girl, and I know it's hard, but we will prevail. Tip for you: keep a positive thoughts journal to help you combat those negative feelings.");
    st.subheader("Share Your Story")
    name = st.text_input("Your Name")
    title = st.text_input("Title of Your Story")
    content = st.text_area("Write your story here...")
