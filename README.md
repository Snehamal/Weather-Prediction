# 🌤️ Weather App

A full-stack weather application that lets users search for cities and view live current weather and a 5-day forecast. Built with a **Python (Flask) backend** and a **React + TypeScript** frontend, powered by the free [Open-Meteo](https://open-meteo.com/) API.

## Features

- 🔍 Search and filter cities
- 🌡️ Live current weather (temperature, wind speed, condition)
- 📅 5-day forecast with daily high/low and weather icons
- ⭐ Mark cities as favorites for quick access
- 🌡️ Toggle between °C and °F
- 🎨 Background theme changes dynamically based on current weather
- 🔄 Manual refresh + "last updated" timestamp
- 💀 Loading skeletons and clear error handling with retry

## Tech Stack

| Layer     | Technology |
|-----------|------------|
| Backend   | Python, Flask, Flask-CORS |
| Frontend  | React, TypeScript, Vite |
| Weather Data | [Open-Meteo API](https://open-meteo.com/) (free, no API key required) |

## Project Structure

```
weather-app/
├── backend/
│   ├── app.py            # Flask API (cities + weather + forecast endpoints)
│   ├── cities.json       # Static list of supported cities
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── src/
        ├── main.tsx
        ├── App.tsx        # Main UI component
        ├── api.ts         # API call helpers
        ├── types.ts        # Shared TypeScript types
        ├── weatherUtils.ts # Weather icon/theme helpers
        └── index.css
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| GET | `/` | Welcome message + list of available endpoints |
| GET | `/api/cities` | Returns the list of cities from `cities.json` |
| GET | `/api/weather?city_id=<id>` | Returns current weather for the given city |
| GET | `/api/forecast?city_id=<id>` | Returns a 5-day forecast for the given city |

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+

### 1. Run the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
The API will be available at `http://localhost:5000`.

### 2. Run the frontend
In a new terminal:
```bash
cd frontend
npm install
npm run dev
```
Open the URL Vite prints (usually `http://localhost:5173`).

## How It Works

1. `cities.json` stores a static list of supported cities (name, country, coordinates).
2. The React frontend calls `GET /api/cities` to populate the city list.
3. When a city is selected, the frontend calls `GET /api/weather` and `GET /api/forecast`.
4. The Flask backend looks up the city's coordinates and forwards the request to Open-Meteo, then returns clean, simplified JSON to the frontend.
5. The frontend renders the current conditions, a 5-day forecast strip, and adjusts its background theme based on the weather code returned.

## Possible Future Improvements

- Add geolocation ("use my current location")
- Add hourly forecast charts
- Persist favorites and unit preference across sessions
- Add dark mode toggle

## License

This project is open source and available for learning/demo purposes.
