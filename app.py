import streamlit as st
from functions import *

with st.sidebar:
    open_api_key = st.text_input("Open AI API key", type='password')

if not open_api_key:
    st.warning("Please enter a valid Open AI API key.")
    st.stop()
st.session_state["api_key"] = open_api_key

st.title("Talk with your IFC")
st.write("Share your IFC and ask what is happening")

uploaded_file = st.file_uploader("Upload file", type=(".ifc"))

df = functions.transform_ifc_to_df(uploaded_file)

question = st.text_input(
    "Ask something about filee",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)








#! TODO
"https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/"
# next step

