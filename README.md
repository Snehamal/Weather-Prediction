# Weather App

A full-stack weather app:
- **Backend:** Python (Flask) — reads city list from `cities.json` and fetches live weather from the free [Open-Meteo](https://open-meteo.com/) API (no API key needed).
- **Frontend:** React + TypeScript (Vite) — lets the user pick a city and shows current weather.

## Project Structure
```
weather-app/
├── backend/
│   ├── app.py            # Flask API
│   ├── cities.json       # Static list of cities
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── api.ts
        ├── types.ts
        └── index.css
```

## 1. Run the Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The API runs at `http://localhost:5000`.

**Endpoints:**
- `GET /api/cities` → list of cities from `cities.json`
- `GET /api/weather?city_id=1` → live current weather for that city

## 2. Run the Frontend

In a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`).

## How It Works
1. `cities.json` holds the static list of cities (id, name, country, lat/lon).
2. The React app calls `GET /api/cities` to populate the dropdown.
3. When a city is selected, the React app calls `GET /api/weather?city_id=...`.
4. The Flask backend looks up the city's coordinates and calls the Open-Meteo API to get live weather, then returns clean JSON to the frontend.

## Extending This Project
- Swap Open-Meteo for OpenWeatherMap/WeatherAPI by changing the request in `app.py` (you'd need an API key for those).
- Add more cities to `cities.json` — no code changes needed.
- Add a search box instead of a dropdown.
- Persist favorite cities using `localStorage` (or a small database on the backend).
- Add a 5-day forecast using Open-Meteo's `daily` parameters.
