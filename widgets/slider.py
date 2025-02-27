import streamlit as st
x = st.slider('Select x value')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
