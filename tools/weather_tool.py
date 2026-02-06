import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    if not city:
        return "Weather tool error: city not provided"

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            message = data.get("message", "Unknown error")
            return f"Weather API error: {message}"

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"{city} weather: {temp}°C, {description}"

    except Exception as e:
        return f"Weather tool error: {str(e)}"
