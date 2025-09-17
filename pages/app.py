import streamlit as st
import pandas as pd
import openpyxl

st.title("Planet Mark Submission Calculator")

help_page = st.Page("get_started.py", title="Get started")
data_page = st.Page("calculate_data.py", title="Calculate data")


pg = st.navigation([help_page, data_page])
pg.run()