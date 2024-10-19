import streamlit as st

# Function to connect people to buddies
def buddy():
  Buddies = {'Cancer': ['Alice', 'Ben', 'Jaspreet', 'Donald', 'June'] , 'Depression': ['Bernard', 'Andrew', 'Melaina', 'Carl'], 'Diabetes': ['Delian', 'Sally'], 'Eating Disorder': ['Dennis', 'Julia']}
  st.title("Find a Health Buddy")
  st.write("Please input your name and health concern you would like to connect with a buddy over.")
  name = st.text_input("Your Name")
  health_options = ['Cancer', 'Depression', 'Diabetes', 'Eating Disorder']
  selected_value = st.selectbox('Select a health concern:', health_options)
  submit_clicked = st.button("Submit")
  if submit_clicked:
    if name and selected_value:
      for key in Buddies:
        st.write("Here are some people you can connect with: " + key)
