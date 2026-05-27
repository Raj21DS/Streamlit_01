import streamlit as st
import requests

st.set_page_config(layout = "wide")
st.write("Hello World")
x = st.text_input("Favourite Movie?")
st.write(f"your favourite movie is: {x}")
st.write("## This is a H2 Title")
stream_url ="https://www.youtube.com/watch?v=D1eL1EnxXXQ"
st.video(stream_url)

