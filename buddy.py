import streamlit as st

# Function to connect people to buddies
def buddy():

  if 'selected_value' not in st.session_state:
        st.session_state.selected_value = None
  if 'buddies_list' not in st.session_state:
        st.session_state.buddies_list = []
      
  Buddies_Description = {
      'Cancer': ['At 34, I never expected to face breast cancer, but after my diagnosis last year, I discovered a strength I didn’t know I had. Now that I’m on the other side, I want to share my journey through my blog to help others find hope. I’m eager to connect with someone who’s currently facing this challenge and offer my support.', 'As a school teacher, I’ve always believed in the power of laughter, which helped me immensely during my battle with stage 2 colon cancer. Now, at 45, I’m ready to share my experiences and the lighter moments from my journey. I’m looking to connect with someone who could use a buddy to help navigate this tough road.', 'Art has always been my refuge, and it became even more important during my fight with ovarian cancer. I’m Jaspreet, 28, and now that I’ve come through it, I’m passionate about using my art to inspire others. I’m hoping to connect with someone who needs encouragement and a friend to share their story.', 'Having served as a veteran, I thought I had faced my toughest battles. Then I was diagnosed with prostate cancer at 60. Now that I’m in recovery, I want to give back by sharing what I’ve learned about resilience and mental strength. I’m here to support someone who’s currently navigating their journey.', 'As a grandmother, I’ve always cherished family moments, but my lung cancer diagnosis changed my perspective on life. At 50, I’ve learned the importance of community and support. I want to connect with someone who’s going through a similar experience, offering both practical advice and emotional support as a fellow survivor.'],
      'Depression': ['I’m Bernard, and my journey with depression began unexpectedly during my late 30s. As a passionate musician, I found solace in writing songs, which helped me express my emotions. Now that I’ve learned to manage my mental health, I want to support others who are struggling. I’m here to connect with someone who needs encouragement and understanding.', 'Hi, I’m Andrew. After years of dealing with anxiety and depression, I’ve come to realize the importance of sharing my story. I’m 42 and have found healing through mindfulness and community support. I want to help others find their path to recovery and connect with someone who feels isolated in their journey.', 'I’m Melaina, and I’m 30 years old. My battle with depression started in college, but through therapy and self-care, I’ve learned valuable coping strategies. I’m passionate about mental health advocacy and want to connect with someone who feels overwhelmed. Together, we can share our experiences and support each other.', 'I’m Carl, a 50-year-old father of three. After experiencing a tough period of depression, I realized how important it is to talk about mental health openly. I’ve learned to lean on my family and friends, and now I’m committed to helping others navigate their own challenges. I’d love to connect with someone who’s looking for a buddy to share their journey with.'],
      'Diabetes': ['I’m Delian, and I was diagnosed with type 1 diabetes at 22. At first, it felt overwhelming, but I’ve learned to manage my condition through careful planning and support. I’m passionate about educating others about diabetes management and would love to connect with someone who is newly diagnosed or struggling with their journey.', 'Hi, I’m Sally. Living with type 2 diabetes has taught me the importance of a balanced lifestyle. I was diagnosed five years ago, and I’ve made it my mission to share my experiences with nutrition and exercise. I’m here to support anyone who feels lost or needs guidance in managing their diabetes.', 'I’m Payal, and I’ve been living with diabetes for over a decade. As a health coach, I believe in empowering others to take control of their health. I’ve faced many ups and downs, and I want to connect with someone who needs encouragement and practical tips to navigate their diabetes journey. Together, we can create a supportive community.'],
      'Eating Disorder': ['I’m Dennis, and my journey with an eating disorder began in my teens. After years of struggle, I found recovery through therapy and support groups. Now at 29, I’m passionate about helping others understand that recovery is possible. I want to connect with someone who needs encouragement and a listening ear.', 'Hi, I’m Julia. I battled bulimia for most of my twenties, but I’m proud to say I’ve been in recovery for two years. I’ve learned the importance of self-compassion and healthy coping mechanisms. I’d love to connect with someone who is struggling and show them that they’re not alone in this fight.', 'I’m Luna, and I’ve experienced the challenges of an eating disorder since I was 16. Now at 24, I focus on using my experience to support others. I believe in the power of community and sharing our stories. I’m here to connect with anyone who needs support and understanding on their journey to recovery.', 'I’m Joey, a 35-year-old who has been in recovery from binge eating disorder for several years. My journey has taught me the importance of balance and self-acceptance. I’m committed to helping others navigate their challenges and would love to connect with someone looking for a buddy to share their experiences with.']
  }
  Buddies = {
        'Cancer': ['Alice', 'Ben', 'Jaspreet', 'Donald', 'June'],
        'Depression': ['Bernard', 'Andrew', 'Melaina', 'Carl'],
        'Diabetes': ['Delian', 'Sally', 'Payal'],
        'Eating Disorder': ['Dennis', 'Julia', 'Luna', 'Joey']
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
      
      people_options = st.selectbox('Select a person to connect with:', st.session_state.buddies_list)
      if people_options:
        connect = st.button("Connect!")
          if connect:
              st.write("We sent an email requesting your connection. You will be connected with your buddy soon!")

