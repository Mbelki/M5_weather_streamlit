import os
from dotenv import load_dotenv
import requests

# Assurez-vous que la fonction get_outdoor_weather est dans ce fichier ou importez-la si elle est dans un autre module
# from your_module import get_outdoor_weather

load_dotenv()
WEATHER_API = os.getenv('WEATHER_API')
WEATHER_URL = "http://api.weatherapi.com/v1/forecast.json"

def get_outdoor_weather():
    params = {
        "key": WEATHER_API,
        "q": "Lausanne",
        "days": 3,  # Nombre de jours de prévision
        "aqi": "no"
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        current_weather = {
            "temperature_c": data['current']['temp_c'],
            "condition_text": data['current']['condition']['text'],
            "icon_url": "https:" + data['current']['condition']['icon']
        }
        # Ajout de prévisions
        forecast_data = []
        for day in data['forecast']['forecastday']:
            forecast_data.append({
                "date": day['date'],
                "max_temp": day['day']['maxtemp_c'],
                "min_temp": day['day']['mintemp_c'],
                "condition_text": day['day']['condition']['text'],
                "icon_url": "https:" + day['day']['condition']['icon']
            })

        return {
            "current_weather": current_weather,
            "forecast": forecast_data
        }
    else:
        return {"error": "Failed to fetch weather data"}

def main():
    weather_data = get_outdoor_weather()
    print(weather_data)

if __name__ == "__main__":
    main()
