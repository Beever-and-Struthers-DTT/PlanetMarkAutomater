import streamlit as st

st.set_page_config(page_title="Feedback")


with st.form("feedback_form"):
    st.write("Inside the form")
    slider_val = st.slider("On a scale of 1-10 how likely are you to use this form again?", 1, 10)
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Thanks for the feedback!")
