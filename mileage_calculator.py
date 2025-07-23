import os
import pandas as pd
import openpyxl

file_path = "TravelInfo.xlsx"
dfs = []
pd.options.display.width = 0
pd.options.display.max_rows = 999

#Rates to calculate mileage


for sheet_name, df in pd.read_excel(r"TravelInfo.xlsx", index_col=0, sheet_name=None).items():
    combined_df = pd.concat([df], ignore_index=True)

#print(combined_df)

# print('-------------------------------------------------------------------------')
# sage_df = pd.read_excel(r"TravelInfo.xlsx", index_col=0, sheet_name='Sage NL Downloads 7400 7420')
# print(sage_df)
#

print('-----------------------------------------------------------------------------')

PE_df = pd.read_excel(r"TravelInfo.xlsx", index_col=0, sheet_name='Non-Chg')
#print(PE_df)

grouped = PE_df.groupby(PE_df.WIP_Analysis)
single_noncharge_mileage = grouped.get_group('Mileage 45p Non-chargeable')
shared_noncharge_mileage = grouped.get_group('Mileage 50p Non-chargeable')

single_noncharge_miles = ((single_noncharge_mileage['WIP_Amount'].sum()) / 0.55).round(2)
shared_noncharge_miles = ((shared_noncharge_mileage['WIP_Amount'].sum()) / 0.55).round(2)

total_non_charge_miles = single_noncharge_miles + shared_noncharge_miles
print('Total non-chargeable miles:', total_non_charge_miles)

hotel_expenses = grouped.get_group('Hotel Accomodation Non-chargeable')
total_noncharge_hotel_costs = (hotel_expenses['WIP_Amount'].sum()).round(2)
print('Total non-chargeable hotel accomodation costs:', total_noncharge_hotel_costs)

print('-----------------------------------------------------------------------------')
PE_df = pd.read_excel(r"TravelInfo.xlsx", index_col=0, sheet_name='Chg')
#print(PE_df)

grouped = PE_df.groupby(PE_df.WIP_Analysis)
single_charge_mileage = grouped.get_group('Mileage 45p Chargeable')
shared_charge_mileage = grouped.get_group('Mileage 50p Chargeable')
#print(mileage)

single_charge_miles = ((single_charge_mileage['WIP_Amount'].sum()) / 0.55).round(2)
shared_charge_miles = ((shared_charge_mileage['WIP_Amount'].sum()) / 0.55).round(2)

total_chargable_miles = single_charge_miles + shared_charge_miles
print('Total chargeable miles:', total_chargable_miles)

hotel_expenses = grouped.get_group('Hotel Accomodation Chargeable')
total_charge_hotel_costs = (hotel_expenses['WIP_Amount'].sum()).round(2)
print('Total chargeable hotel accomodation costs:', total_charge_hotel_costs)
print('-----------------------------------------------------------------------------')
total_single_miles = single_noncharge_miles + single_charge_miles
print('Total solo miles:', total_single_miles)

total_shared_miles = shared_noncharge_miles + shared_charge_miles
print('Total pooled miles:', total_shared_miles)

total_hotel_costs = total_noncharge_hotel_costs + total_charge_hotel_costs
print('Total hotel costs:', total_hotel_costs)