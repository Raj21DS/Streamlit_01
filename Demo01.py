import streamlit as st

st.set_page_config(layout = "wide")
st.write("Hello World")
x = st.text_input("Favourite Movie?")
st.write(f"your favourite movie is: {x}")
st.write("## This is a H2 Title")

