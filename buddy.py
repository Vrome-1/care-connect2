import streamlit as st

# Function to connect people to buddies
def buddy():

  if 'selected_value' not in st.session_state:
        st.session_state.selected_value = None
  if 'buddies_list' not in st.session_state:
        st.session_state.buddies_list = []
      
  Buddies_Description = {
      'Cancer': ['At 34, I never expected to face breast cancer, but after my diagnosis last year, I discovered a strength I didn’t know I had. Now that I’m on the other side, I want to share my journey through my blog to help others find hope. I’m eager to connect with someone who’s currently facing this challenge and offer my support.', 'As a school teacher, I’ve always believed in the power of laughter, which helped me immensely during my battle with stage 2 colon cancer. Now, at 45, I’m ready to share my experiences and the lighter moments from my journey. I’m looking to connect with someone who could use a buddy to help navigate this tough road.', 'Art has always been my refuge, and it became even more important during my fight with ovarian cancer. I’m Jaspreet, 28, and now that I’ve come through it, I’m passionate about using my art to inspire others. I’m hoping to connect with someone who needs encouragement and a friend to share their story.', 'Having served as a veteran, I thought I had faced my toughest battles. Then I was diagnosed with prostate cancer at 60. Now that I’m in recovery, I want to give back by sharing what I’ve learned about resilience and mental strength. I’m here to support someone who’s currently navigating their journey.', 'As a grandmother, I’ve always cherished family moments, but my lung cancer diagnosis changed my perspective on life. At 50, I’ve learned the importance of community and support. I want to connect with someone who’s going through a similar experience, offering both practical advice and emotional support as a fellow survivor.'],
      'Depression': ['Bernard', 'Andrew', 'Melaina', 'Carl'],
      'Diabetes': ['Delian', 'Sally'],
      'Eating Disorder': ['Dennis', 'Julia']
  }
  Buddies = {
        'Cancer': ['Alice', 'Ben', 'Jaspreet', 'Donald', 'June'],
        'Depression': ['Bernard', 'Andrew', 'Melaina', 'Carl'],
        'Diabetes': ['Delian', 'Sally'],
        'Eating Disorder': ['Dennis', 'Julia']
  }
  
  st.title("Find a Health Buddy")
  st.write("Please input your name and health concern you would like to connect with a buddy over.")
  name = st.text_input("Your Name")
  email = st.text_input("Your Email")
  health_options = ['Cancer', 'Depression', 'Diabetes', 'Eating Disorder']
  st.session_state.selected_value = st.selectbox('Select a health concern:', health_options)
  submit_clicked = st.button("Submit")
  if submit_clicked:
    if name and st.session_state.selected_value:
      st.write("Here are some people you can connect with: ")
      for key in Buddies:
        if (key == st.session_state.selected_value): 
          st.session_state.buddies_list = Buddies[st.session_state.selected_value]
          st.session_state.buddies_description_list = Buddies_Description[st.session_state.selected_value]
          for person, description in zip(st.session_state.buddies_list,st.session_state.buddies_description_list):
            st.markdown(
                f"""
                <div style="background-color: #f0f2f5; padding: 20px; border-radius: 5px; border: 1px solid #ccc;">
                <h4 style="color: #000;">{person}</h4>
                <p style="color: #000;">{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
      if st.session_state.buddies_list:
        people_options = st.selectbox('Select a person to connect with:', st.session_state.buddies_list)
        connect = st.button("Connect!")
        if connect:
            st.write("We sent an email requesting your connection. You will be connected with your buddy soon!")

