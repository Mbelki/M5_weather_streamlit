import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from weather import get_last_indoor_weather, display_weather_app, display_indoor_weather, fetch_weather_data
from settings import update_user_name, get_current_user_name, get_wifi_settings, submit_new_wifi
load_dotenv()

st.title("Weather Data Management")
    
st.header("Outdoor Weather", divider='blue')
display_weather_app()

st.header("Last Indoor Weather", divider='blue')
display_indoor_weather(get_last_indoor_weather())


        
        

        
 