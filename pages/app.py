import streamlit as st
import pandas as pd

st.title("Planet Mark Submission Calculator")

data_page = st.Page("calculate_data.py", title="Calculate data")
feedback_page = st.Page("feedback.py", title="Feedback")

st.sidebar.header("Page navigation")
pg = st.navigation([data_page, feedback_page])
pg.run()