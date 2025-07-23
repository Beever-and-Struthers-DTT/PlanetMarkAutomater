import streamlit as st


st.set_page_config(page_title="Practice Engine data")
st.sidebar.header("Upload your data here")

uploaded_file = st.file_uploader("Upload the Excel sheet here")