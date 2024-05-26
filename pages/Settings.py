import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from weather import get_last_indoor_weather, display_weather_app, display_indoor_weather, fetch_weather_data
from settings import update_user_name, get_current_user_name, get_wifi_settings, submit_new_wifi
load_dotenv()

st.title("Settings")

#input name
st.header("Current User Name")

# Récupérer et afficher le nom de l'utilisateur actuel
user_name = get_current_user_name()
if user_name:
    st.write(f"Current User: {user_name}")


st.header("Enter your name for personalized experience with the app.")
name = st.text_input("Enter your name", "")
if st.button("Submit"):
    if name:
        update_user_name(name)
    else:
        st.warning("Please enter a name before submitting.")
        
        
st.title('WiFi Configuration')
st.write("check current WiFi settings in the list below")

if st.button('Get Current WiFi Settings'):
    wifi_settings_list = get_wifi_settings()
    if wifi_settings_list:
        for wifi in wifi_settings_list:
            st.write(f"Current WiFi SSID: {wifi.get('name')}")
            st.write(f"Current WiFi Password: {wifi.get('password')}")
            st.write("---") 
            
st.write("## Update WiFi Settings")
ssid = st.text_input("WiFi SSID")
password = st.text_input("WiFi Password", type="password")

if st.button('Update WiFi'):
    submit_new_wifi(ssid, password)