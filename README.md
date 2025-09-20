# Live Aviation Data Dashboard  

A real-time dashboard for tracking global flights, built with **FastAPI**, **Python REST APIs**, and a **Leaflet.js frontend**.  

This project processes and visualizes live **aircraft telemetry** and **weather data**, with features like:  
- Real-time flight tracking  
- Filterable flight lists  
- Airline toggles  
- Trajectory plotting  
- Integrated live weather map layers  

---

## Demo  

### Screenshots  
| Flight List & Filters | Trajectory Plotting | Weather Overlay |  
|----------------------|---------------------|----------------|  
| ![Flight list screenshot](screenshots/flight_list.png) | ![Trajectory plotting screenshot](screenshots/trajectory.png) | ![Weather overlay screenshot](screenshots/weather.png) |  


### GIF / Video Demo  
Sometimes a GIF or short video says it best. You can drop in a screen recording here:  

- **GIF:**  
  ![Dashboard demo](screenshots/dashboard_demo.gif)  

- **Video (optional):**  
  [▶️ Watch the demo](https://your-link-here.com)  

---

## Tech Stack  

- **Backend:** Python, FastAPI, REST APIs  
- **Frontend:** JavaScript, Leaflet.js  
- **Data Sources:**  
  - [OpenSky Network API](https://opensky-network.org/) for live flight data  
  - [OpenWeather API](https://openweathermap.org/api) for weather overlays  

---

## Usage Instructions


Follow these steps to run the dashboard locally:  

### 1. Clone the repository  
```bash
git clone https://github.com/gabriella-lewis/flight-dashboard.git
```

### 2. Install dependencies
Install all python packages applicable for this project:
```bash
pip install requirements.txt
```


### 3. Configure API credentials

Create a .env file in the project root with your credentials:

```bash
# .env file
OPEN_SKY_USERNAME=your_opensky_username
OPEN_SKY_PASSWORD=your_opensky_password
WEATHER_API_KEY=your_openweather_api_key
```

OpenSky Network API: Create a free account [here](https://opensky-network.org/)

OpenWeather API: Get a free key [here](https://openweathermap.org/api)

### 4. Run the backend server
```bash
fastapi dev app.py
```


By default, the API will be available at:

http://localhost:8000

### 5. Launch the frontend

Open the frontend file in your browser:

http://localhost:8000/index.html


You should now see the dashboard with live flight and weather data
