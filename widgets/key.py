import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.write("Hello, ", st.session_state.name)

# You can also store in variable
name =st.session_state.name
"How are you, ", st.session_state.name, "?"