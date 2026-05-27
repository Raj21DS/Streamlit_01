import streamlit as st
import requests

st.set_page_config(layout = "wide")
st.write("Hello World")
x = st.text_input("Favourite Movie?")
st.write(f"your favourite movie is: {x}")
st.write("## This is a H2 Title")
stream_url ="https://www.youtube.com/watch?v=D1eL1EnxXXQ"
st.video(stream_url)

response = requests.get(stream_url, params=params)
data = response.json()

if "items" in data and len(data["items"]) > 0:
  stats = data["items"][0]["statistics"]
# return 
    "views": stats.get("viewCount", 0),
    "likes": stats.get("likeCount", 0),
    "comments": stats.get("commentCount", 0)
        
# return None
st.write(f"👁 Views: {stats['views']}")
st.write(f"👍 Likes: {stats['likes']}")
st.write(f"💬 Comments: {stats['comments']}")
