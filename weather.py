import os
import streamlit as st
from dotenv import load_dotenv
import requests
import pandas as pd
load_dotenv()

token = os.getenv("SECRET_TOKEN")

# Configuration
BACKEND_URL = "https://backend-ukfss2zija-oa.a.run.app"

headers = {
    "Authorization": token
}

def get_outdoor_weather():
    """
    Retrieve the current outdoor weather and forecast from the backend.

    Returns:
        dict: A dictionary containing the current weather and forecast data or an error message.
    """
    response = requests.get(f"{BACKEND_URL}/get_outdoor_weather", headers=headers)
    if response.status_code == 200:
        try:
            # Tenter de décoder la réponse JSON
            return response.json()
        except ValueError:
            # Gérer le cas où la réponse ne contient pas de JSON valide
            return {"error": "No valid JSON response"}
    else:
        # Retourner un message ou le code de statut pour indiquer l'erreur
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}


def get_last_indoor_weather():
    """
    Retrieve the last recorded indoor weather data from the backend.

    Returns:
        dict: A dictionary containing the indoor weather data or an error message.
    """
    response = requests.get(f"{BACKEND_URL}/get_last_indoor_weather", headers= headers)
    if response.status_code == 200:
        try:
            # Tenter de décoder la réponse JSON
            return response.json()
        except ValueError:
            # Gérer le cas où la réponse ne contient pas de JSON valide
            return {"error": "No valid JSON response"}
    else:
        # Retourner un message ou le code de statut pour indiquer l'erreur
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

def display_weather_app():
    """
    Display the current outdoor weather and forecast using data retrieved from the API.
    """
    weather_data = get_outdoor_weather()

    if "error" not in weather_data:
        st.subheader('Current Weather')
        current_weather = weather_data['current_weather']
        col1, col2 = st.columns(2)
        with col1:
            st.image(current_weather['icon_url'], width=100)
        with col2:
            st.subheader(current_weather['condition_text'])
            st.write(f"Temperature: {current_weather['temperature_c']}°C")

        st.subheader('Weather Forecast', divider='grey')
        for forecast in weather_data['forecast']:
            cols = st.columns(3)
            with cols[0]:
                st.image(forecast['icon_url'], width=100)
                st.caption(forecast['date'])
            with cols[1]:
                st.metric(label="Max Temp", value=f"{forecast['max_temp']}°C")
            with cols[2]:
                st.metric(label="Min Temp", value=f"{forecast['min_temp']}°C")
                st.caption(forecast['condition_text'])
    else:
        st.error("Failed to fetch weather data")

def display_indoor_weather(data):
    """
    Display the current indoor weather data.

    Args:
        data (dict): A dictionary containing indoor weather data or an error message.
    """
    if "error" not in data:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Temperature", value=f"{data['temperature']} °C", delta_color="off")
        with col2:
            st.metric(label="Humidity", value=f"{data['humidity']} %", delta_color="off")
        with col3:
            st.metric(label="Pressure", value=f"{data['pressure']} hPa", delta_color="off")
        with col4:
            st.metric(label="co2", value=f"{data['co2']}", delta_color="off")
    else:
        st.error(data["error"])

def fetch_weather_data():
    """
    Fetch mean indoor weather data from the Flask backend.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the mean indoor weather data or an empty DataFrame if the request fails.
    """
    response = requests.get(f"{BACKEND_URL}/get_mean_indoor_weather", headers= headers)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error("Failed to fetch weather data.")
        return pd.DataFrame()
