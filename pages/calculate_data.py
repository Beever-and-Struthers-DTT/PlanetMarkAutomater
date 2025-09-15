import pandas as pd
import streamlit as st
import openpyxl


st.set_page_config(page_title="Practice Engine data")


uploaded_file = st.file_uploader("Upload the Excel sheet here")

if uploaded_file is not None:
    global df
    for sheet_name, df in pd.read_excel(r"TravelInfo.xlsx", index_col=0, sheet_name=None).items():
        combined_df = pd.concat([df], ignore_index=True)

    st.dataframe(combined_df)