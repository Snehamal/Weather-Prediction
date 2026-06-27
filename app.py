"""
Weather App Backend
--------------------
- Reads a static list of cities from cities.json
- Fetches live weather for a city from the free Open-Meteo API
  (https://open-meteo.com/ - no API key required)

Endpoints:
  GET /                          -> welcome message + endpoint list
  GET /api/cities                -> list of cities from cities.json
  GET /api/weather?city_id=1     -> current weather for that city
"""

import json
import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow the React dev server (different port) to call this API

CITIES_FILE = os.path.join(os.path.dirname(__file__), "cities.json")

# Open-Meteo weather codes -> human readable description
WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Freezing fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
}


def load_cities():
    with open(CITIES_FILE, "r") as f:
        return json.load(f)


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Weather App API is running",
        "endpoints": {
            "cities": "/api/cities",
            "weather": "/api/weather?city_id=1"
        }
    })


@app.route("/api/cities", methods=["GET"])
def get_cities():
    return jsonify(load_cities())


@app.route("/api/weather", methods=["GET"])
def get_weather():
    city_id = request.args.get("city_id", type=int)
    cities = load_cities()
    city = next((c for c in cities if c["id"] == city_id), None)

    if city is None:
        return jsonify({"error": "City not found"}), 404

    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": city["lat"],
                "longitude": city["lon"],
                "current_weather": "true",
                "timezone": "auto",
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        current = data.get("current_weather", {})

        result = {
            "city": city["name"],
            "country": city["country"],
            "temperature_c": current.get("temperature"),
            "windspeed_kmh": current.get("windspeed"),
            "weather_code": current.get("weathercode"),
            "description": WEATHER_CODES.get(current.get("weathercode"), "Unknown"),
            "observed_at": current.get("time"),
        }
        return jsonify(result)

    except requests.RequestException as e:
        return jsonify({"error": f"Failed to fetch weather: {str(e)}"}), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)