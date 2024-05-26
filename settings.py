import os
import streamlit as st
from dotenv import load_dotenv
import requests
from API_weather import get_outdoor_weather
load_dotenv()

token = os.getenv("SECRET_TOKEN")

# Configuration
BACKEND_URL = "https://backend-ukfss2zija-oa.a.run.app"

headers = {
    "Authorization": token
}

def update_user_name(name):
    response = requests.post(f"{BACKEND_URL}/update_current_user_name", headers= headers, json={"name": name})
    if response.status_code == 200:
        st.success("Name added successfully!")
    else:
        st.error("Failed to add name to the database.")

def get_current_user_name():
    response = requests.get(f"{BACKEND_URL}/get_current_user_name", headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("name", "No name found")
    else:
        st.error("Failed to fetch the current user's name.")
        return None
    
def get_wifi_settings():
    """Fetch WiFi settings from the Flask backend."""
    response = requests.get(f"{BACKEND_URL}/get_wifi", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch WiFi settings.')
        return None

def submit_new_wifi(name, password):
    """Submit new WiFi settings to the Flask backend."""
    response = requests.post(f"{BACKEND_URL}/add_wifi", json={'name': name, 'password': password}, headers=headers)
    if response.status_code == 200:
        st.success('WiFi settings updated successfully.')
    else:
        st.error('Failed to update WiFi settings.')