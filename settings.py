import os
import streamlit as st
from dotenv import load_dotenv
import requests
from weather import get_outdoor_weather
load_dotenv()

token = os.getenv("SECRET_TOKEN")

# Configuration
BACKEND_URL = "https://backend-ukfss2zija-oa.a.run.app"

headers = {
    "Authorization": token
}

def update_user_name(name):
    """
    Update the user's name.

    Args:
        name (str): The new name to set for the user.
    """
    response = requests.post(f"{BACKEND_URL}/update_current_user_name", headers= headers, json={"name": name})
    if response.status_code == 200:
        st.success("Name added successfully!")
    else:
        st.error("Failed to add name to the database.")

def get_current_user_name():
    """
    Retrieve the current user's name.

    Returns:
        str: The name of the current user.
    """
    response = requests.get(f"{BACKEND_URL}/get_current_user_name", headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("name", "No name found")
    else:
        st.error("Failed to fetch the current user's name.")
        return None
    
def get_wifi_settings():
    """
    Retrieve the current WiFi settings.

    Returns:
        list: A list of dictionaries containing WiFi settings, each with 'name' and 'password' keys.
    """
    response = requests.get(f"{BACKEND_URL}/get_wifi", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch WiFi settings.')
        return None

def submit_new_wifi(name, password):
    """
    Submit new WiFi settings.

    Args:
        ssid (str): The SSID of the WiFi network.
        password (str): The password for the WiFi network.
    """
    response = requests.post(f"{BACKEND_URL}/add_wifi", json={'name': name, 'password': password}, headers=headers)
    if response.status_code == 200:
        st.success('WiFi settings updated successfully.')
    else:
        st.error('Failed to update WiFi settings.')