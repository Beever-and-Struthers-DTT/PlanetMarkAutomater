import streamlit as st

st.set_page_config(page_title="Get started")

st.write("In order for the Calculator to run smoothly, some pre-processing is required on the data. "
         "Please follow these instructions to ensure your file can be read!")

st.subheader("Step 1", divider=True)
st.write("Ensure that the sheet names are named as such:")
st.image("SheetNames.png")
st.write("Extra sheets may be deleted.")

st.subheader("Step 2", divider=True)
st.markdown('''This step is only for the **Non-Chg** and **Chg** sheets.

Change the column names for *WIP Amount* and *WIP Analysis* to *WIP_Amount* and *WIP_Analysis*.
''')
st.image("ColumnNames.png")

st.subheader("Step 3", divider=True)
st.markdown('''This applies to the **Sage downloads** sheet only.

Remove the extra rows at the top of the sheet, so that the table columns is the first bit of data read by the calculator.''')
st.image("SageTableHeadersBefore.png", caption="Before")
st.write("Please leave the first row of the sheet empty, as shown below.")
st.image("SageTableHeadersAfter.png", caption="After")