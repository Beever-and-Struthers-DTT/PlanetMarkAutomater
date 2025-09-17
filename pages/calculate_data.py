import numpy as np
import pandas as pd
import streamlit as st



st.set_page_config(page_title="Practice Engine data")


uploaded_file = st.file_uploader("Upload the Excel sheet here")

if uploaded_file is not None:
    #global df
    # for sheet_name, df in pd.read_excel(r"TravelInfo.xlsx", index_col=0, sheet_name=None).items():
    #     combined_df = pd.concat([df], ignore_index=True)

    #st.dataframe(combined_df)
    st.subheader("Non-chargeable expenses", divider=True)
    PE_df = pd.read_excel(uploaded_file, index_col=0, sheet_name='Non-Chg')
    # print(PE_df)

    grouped = PE_df.groupby(PE_df.WIP_Analysis)
    single_noncharge_mileage = grouped.get_group('Mileage 45p Non-chargeable')
    shared_noncharge_mileage = grouped.get_group('Mileage 50p Non-chargeable')

    single_noncharge_miles = ((single_noncharge_mileage['WIP_Amount'].sum()) / 0.55).round(2)
    shared_noncharge_miles = ((shared_noncharge_mileage['WIP_Amount'].sum()) / 0.55).round(2)

    total_non_charge_miles = single_noncharge_miles + shared_noncharge_miles
    st.write('Total non-chargeable miles by car:', total_non_charge_miles)

    train_taxi_noncharge_mileage = grouped.get_group('Train/Bus/Taxi/Air Fares Non-chargeable')
    train_taxi_noncharge_miles = ((train_taxi_noncharge_mileage['WIP_Amount'].sum()) / 0.55).round(2)
    st.write('Total non-chargeable miles by train and taxi:', train_taxi_noncharge_miles)

    hotel_expenses = grouped.get_group('Hotel Accomodation Non-chargeable')
    total_noncharge_hotel_costs = (hotel_expenses['WIP_Amount'].sum()).round(2)
    st.write('Total non-chargeable hotel accomodation costs:', total_noncharge_hotel_costs)

    print('-----------------------------------------------------------------------------')
    st.subheader("Chargeable expenses", divider=True)
    PE_df = pd.read_excel(uploaded_file, index_col=0, sheet_name='Chg')
    # print(PE_df)

    grouped = PE_df.groupby(PE_df.WIP_Analysis)
    single_charge_mileage = grouped.get_group('Mileage 45p Chargeable')
    shared_charge_mileage = grouped.get_group('Mileage 50p Chargeable')
    # print(mileage)

    single_charge_miles = ((single_charge_mileage['WIP_Amount'].sum()) / 0.55).round(2)
    shared_charge_miles = ((shared_charge_mileage['WIP_Amount'].sum()) / 0.55).round(2)

    total_chargable_miles = single_charge_miles + shared_charge_miles
    st.write('Total chargeable miles by car:', total_chargable_miles)

    train_taxi_charge_mileage = grouped.get_group('Train/Bus/Taxi/Air Fares Chargeable')
    train_taxi_charge_miles = ((train_taxi_charge_mileage['WIP_Amount'].sum()) / 0.55).round(2)
    st.write('Total chargeable miles by train and taxi:', train_taxi_charge_miles)

    hotel_expenses = grouped.get_group('Hotel Accomodation Chargeable')
    total_charge_hotel_costs = (hotel_expenses['WIP_Amount'].sum()).round(2)
    st.write('Total chargeable hotel accomodation costs:', total_charge_hotel_costs)

    print('-----------------------------------------------------------------------------')
    st.subheader("Combined PE expenses", divider=True)
    st.badge("Note: This combines only expenses from PE. "
             "Sage expenses have been calculated separately.", color="orange")

    total_single_miles = single_noncharge_miles + single_charge_miles
    st.write('Total solo miles by car:', total_single_miles.round(2))

    total_shared_miles = shared_noncharge_miles + shared_charge_miles
    st.write('Total pooled miles by car:', total_shared_miles.round(2))

    total_train_taxi_miles = train_taxi_noncharge_miles + train_taxi_charge_miles
    st.write('Total miles by train and taxi:', total_train_taxi_miles.round(2))
    st.caption("Most of these miles will be done via train, however it is impossible to "
               "determine between journeys taken via train/taxi based on the data provided.")

    total_hotel_costs = total_noncharge_hotel_costs + total_charge_hotel_costs
    st.write('Total hotel costs:', total_hotel_costs.round(2))

    print('-----------------------------------------------------------------------------')
    st.subheader("Sage expenses", divider=True)
    st.caption("Note: Sage expenses are non-chargeable.")

    PE_df = pd.read_excel(uploaded_file, index_col=0, sheet_name='Sage NL Downloads 7400 7420')
    # Uses row from Excel to name the columns
    PE_df.columns = PE_df.iloc[0]
    # Removes row used to name df
    PE_df = PE_df.iloc[1:]

    df = PE_df.replace(to_replace=np.nan, value=0)

    total_sage_train_mileage = (df['Trains'].sum() / 0.55).round(2)
    st.write('Total miles by train: ', total_sage_train_mileage)

    total_sage_taxi_mileage = (df['Taxi'].sum() / 2.35).round(2)
    st.write('Total miles by taxi: ', total_sage_taxi_mileage)

    total_sage_car_mileage = (df['Mileage'].sum() / 0.45).round(2)
    st.write('Total miles by car: ', total_sage_car_mileage)
    st.caption("Due to data provided, it is assumed that these trips were solo, and have been calculated as such.")

    total_sage_flight_costs = (df['Flights'].sum()).round(2)
    st.write('Total flight costs: ', total_sage_flight_costs)
    st.caption('To calculate mileage from these flights, the necessary rows are below.')
    flights_df = df.loc[df['Flights'] > 0]
    st.table(flights_df)

    total_sage_hotel_costs = (df['Hotels'].sum()).round(2)
    st.write('Total hotel costs: ', total_sage_hotel_costs)

    print('-----------------------------------------------------------------------------')
    st.subheader("Total expenses", divider=True)
    st.caption("These are the totals from both PE and Sage expenses.")

    st.write('Total miles travelled by car: ', (total_single_miles + total_shared_miles + total_sage_car_mileage))
    st.write('Total miles travelled by train: ', (total_train_taxi_miles + total_sage_train_mileage))
    st.write('Total miles travelled by taxi: ', total_sage_taxi_mileage)
    st.caption("Please note the train/taxi mileage may be inaccurate due to data provided by PE.")
    st.write('Total hotel costs: ', (total_hotel_costs + total_sage_hotel_costs))