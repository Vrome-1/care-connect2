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
      st.write("Here are some people you can connect with: ")
      for key, value in Buddies.items():
        if (key == submit_clicked): 
          buddies_list = Buddies[submit_clicked]
          st.write("Here are some people you can connect with: ")
          st.markdown(
              <div style="background-color: #333; padding: 20px; border-radius: 5px; border: 1px solid #ccc;">
              <h3 style="color: #333;">buddies_list</h3>
              <p style="color: #666;">Connect!</p>
              </div>
              """,
            unsafe_allow_html=True
          )
if __name__ == "__main__":
    buddy()
