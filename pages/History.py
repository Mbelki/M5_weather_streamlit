import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from weather import get_last_indoor_weather, display_weather_app, display_indoor_weather, fetch_weather_data
from settings import update_user_name, get_current_user_name, get_wifi_settings, submit_new_wifi
load_dotenv()

st.title("Weather Data Management")     
df = fetch_weather_data()

if not df.empty:
    # Display charts
    st.write("### Mean Temperature Over Time")
    st.line_chart(df.set_index('hour')['avg_temperature'])

    st.write("### Mean Pressure Over Time")
    st.line_chart(df.set_index('hour')['avg_pressure'])

    st.write("### Mean Humidity Over Time")
    st.line_chart(df.set_index('hour')['avg_humidity'])

else:
    st.write("No data available.")
