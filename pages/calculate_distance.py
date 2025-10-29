import streamlit as st
from geopy import Nominatim, distance


def get_coordinates(place_name):
  geolocator = Nominatim(user_agent="geo_locator")
  location = geolocator.geocode(place_name)
  if location:
    return location.latitude, location.longitude
  else:
    return None, None

st.set_page_config(page_title="Calculate distance")

st.write("Please note that the distance calculator is primarily for calculating the distance"
         " for flight expenses")

with st.form("distance_calculator"):
    start_city = st.text_input("Starting city")
    end_city = st.text_input("Destination city")

    return_flight = st.checkbox("Return flight?")

    submitted = st.form_submit_button("Calculate")
    st.caption("Please note that distance will be calculated to 2 decimal places.")

    if submitted:
        distance_miles = distance.distance(get_coordinates(start_city), get_coordinates(end_city)).miles
        st.write("Distance between ", start_city, " and ", end_city, " is: ", round(distance_miles, 2), " miles.")

        if return_flight:
            st.write("With a return flight, the total distance is ", round((distance_miles * 2), 2), " miles.")
