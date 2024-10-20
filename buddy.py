import streamlit as st

# Function to connect people to buddies
def buddy():

  if 'selected_value' not in st.session_state:
        st.session_state.selected_value = None
  if 'buddies_list' not in st.session_state:
        st.session_state.buddies_list = []
      
  Buddies = {'Cancer': ['Alice', 'Ben', 'Jaspreet', 'Donald', 'June'] , 'Depression': ['Bernard', 'Andrew', 'Melaina', 'Carl'], 'Diabetes': ['Delian', 'Sally'], 'Eating Disorder': ['Dennis', 'Julia']}
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
      for key, value in Buddies.items():
        if (key == st.session_state.selected_value): 
          st.session_state.buddies_list = Buddies[st.session_state.selected_value]
          for person in st.session_state.buddies_list:
            st.markdown(
                f"""
                <div style="background-color: #f0f2f5; padding: 20px; border-radius: 5px; border: 1px solid #ccc;">
                <h3 style="color: #000;">{person}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
      if st.session_state.buddies_list:
        people_options = st.selectbox('Select a person to connect with:', st.session_state.buddies_list)
        connect = st.button("Connect!")
        if connect:
            st.write("We sent an email requesting your connection. You will be connected with your buddy soon!")

