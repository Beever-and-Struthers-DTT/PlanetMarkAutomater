import numpy as np
import pandas as pd
import streamlit as st

#from pages.expense_calculations import calculate_train_mileage

def calculate_train_mileage(column):
    return (column.sum()/0.55).round(2)

st.set_page_config(page_title="Menzies data")

uploaded_file = st.file_uploader("Upload the Excel sheet here")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name=0)

    single_miles = df[df['ExpenseTypeReference'] == 'Business Mileage']
    total_single_miles = single_miles['ActualDistance'].sum().round(2)
    st.write('Total solo miles: ', total_single_miles)

    shared_miles = df[df['ExpenseTypeReference'] == 'Passenger Mileage']
    total_shared_miles = shared_miles['ActualDistance'].sum().round(2)
    st.write('Total pooled miles: ', total_shared_miles)

    train_mileage = df[df['ExpenseTypeReference'] == 'Train Fare']
    #total_train_mileage = (train_mileage['Net£'].sum() / 0.55).round(2)
    total_train_mileage = train_mileage['Net£'].apply(calculate_train_mileage)
    st.write('Total train miles: ', total_train_mileage)

    taxi_mileage = df[df['ExpenseTypeReference'] == 'Taxi']
    total_taxi_mileage = (train_mileage['Net£'].sum() / 2.35).round(2)
    st.write('Total taxi miles: ', total_taxi_mileage)

    hotel_costs = df[df['ExpenseTypeReference'] == 'Accommodation & Subsistence']
    total_hotel_costs = hotel_costs['Net£'].sum().round(2)
    st.write('Total hotel/accomodation expenses: ', total_hotel_costs)