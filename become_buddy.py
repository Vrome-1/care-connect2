import streamlit as st

def become_buddy():
  st.title("Become a Health Buddy")
  st.write("Are you looking to make a meaningful connection while supporting others on their health journeys? Join our community of health buddies!")
  st.write("As a health buddy, you'll have the opportunity to connect with individuals who share similar experiences and challenges. Whether you’ve navigated the complexities of cancer, diabetes, depression, or eating disorders, your insights and support can make a real difference in someone else's life.")
  st.subheader("Why become a health buddy?")
  st.markdown("- Share your story")
  st.markdown("- Join a community")
  st.markdown("- Make an impact and help others in need")
  st.write("Ready to take the first step? Sign up today and be a guiding light for someone in need! Together, we can create a supportive network where everyone feels valued and empowered. Join us and be part of something special!")
  name = st.text_input("Your Name:")
  email = st.text_input("Your Email:")
  health = st.text_input("Your Health Condition:")
  story = st.text_input("Your Story (please include your age and your journey with your health concern, share as much as you are comfortable with):")
  goal = st.text_input("What is Your Goal for Being a Buddy?:")
  days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  st.write("Select your availability:")
  for day in days:
    st.checkbox(day)
  st.radio("Select your preferred meeting method: ", ['email', 'video call', 'in-person meeting', 'all of the above'])
  note = st.text_input("Please tell us if you have any other notes we need to keep in mind:")
  st.subheader("Confidentiality Statement")
  st.write("By participating in the health buddy program, I agree to uphold the following principles of confidentiality:")
  st.markdown("1. Respect for Privacy: I understand that any personal information shared with me by my buddy is private and should be treated with respect. I will not disclose any details about their health condition, personal experiences, or any conversations we have without their explicit consent.")
  st.markdown("2. Safe Environment: I will create a safe and supportive environment for my buddy, ensuring they feel comfortable sharing their thoughts and feelings.")
  st.markdown("3. Limited Sharing: While I may share my own experiences, I will not share my buddy's story or information with anyone else, including friends, family, or social media, unless specifically authorized to do so.")
  st.markdown("4. Commitment to Support: I commit to being a trustworthy companion, offering support and understanding without judgment.")
  st.write("By agreeing to these principles, I recognize the importance of confidentiality in fostering a trusting and supportive relationship.")
  if st.checkbox("I agree to the confidentiality statement"):
    st.write("Select Submit.")
  else:
    st.write("Please agree to the confidentiality statement.")
  submit = st.button("Submit")
  if submit:
    st.write("Thank you for submitting your application to me a health buddy! We will review it soon and let you know the next steps in the process!")
