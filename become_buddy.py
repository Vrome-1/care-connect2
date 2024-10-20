import streamlit as st

def become_buddy():
  st.title("Become a Health Buddy")
  st.write("Are you looking to make a meaningful connection while supporting others on their health journeys? Join our community of health buddies!")
  st.write("As a health buddy, you'll have the opportunity to connect with individuals who share similar experiences and challenges. Whether you’ve navigated the complexities of cancer, diabetes, depression, or eating disorders, your insights and support can make a real difference in someone else's life.")
  st.write("Why become a health buddy?")
  st.markdown("- Share your story")
  st.markdown("- Join a community")
  st.markdown("- Make an impact and help others in need")
  st.write("Ready to take the first step? Sign up today and be a guiding light for someone in need! Together, we can create a supportive network where everyone feels valued and empowered. Join us and be part of something special!")
  name = st.text_input("Your Name:")
  email = st.text_input("Your Email:")
  health = st.text_input("Your Health Condition:")
  story = st.text_input("Your Story (please include your age and your journey with your health concern, share as much as you are comfortable with):")
  goal = st.text_input("What is Your Goal for Being a Buddy?:")
  st.radio("Select your availability:", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
  st.radio("Select your preferred meeting method: ", ['email', 'video call', 'in-person meeting', 'all of the above'])
  note = st.text_input("Please tell us if you have any other notes we need to keep in mind:")
  if st.checkbox("I agree to the confidentiality statement"):
    st.write("This is to protect our patient's privacy.")
  else:
    st.write("Please agree to the confidentiality statement.")
  submit = st.button("Submit")
  if submit:
    st.write("Thank you for submitting your application to me a health buddy! We will review it soon and let you know the next steps in the process!")
