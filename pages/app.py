import streamlit as st

st.title("Planet Mark Submission Calculator")

help_page = st.Page("get_started.py", title="Get started")
PE_page = st.Page("calculate_PE_data.py", title="Calculate PE data")
menzies_page = st.Page("calculate_menzies_data.py", title="Calculate Menzies data")
distance_page = st.Page("calculate_distance.py", title="Calculate distance")


pg = st.navigation([help_page, PE_page, distance_page])
pg.run()