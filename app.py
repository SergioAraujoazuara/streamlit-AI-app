import streamlit as st
 

with st.sidebar:
    open_api_key = st.text_input("Open AI API key", type='password')


st.title("Talk with your IFC")
st.write("Share your IFC and ask whats is happening")

uploaded_file = st.file_uploader("Upload an article", type=(".ifc"))

question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

