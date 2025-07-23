import streamlit as st
import pandas as pd

st.title("Planet Mark Submission Calculator")

st.set_page_config(page_title="Homepage")

st.write("Test")

data_page = st.Page("calculate_data.py", title="Create entry")
feedback_page = st.Page("feedback.py", title="Feedback")
pg = st.navigation([data_page, feedback_page])
pg.run()