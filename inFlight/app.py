import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("OPEN_SKY_CLIENT_ID")
CLIENT_SECRET = os.getenv("OPEN_SKY_CLIENT_SECRET")
API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

def get_opensky_token():
    resp = requests.post(
        "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token",
        data= {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    resp.raise_for_status()
    data = resp.json()
    token = data["access_token"]
    return token

@app.get("/get_flights")
def retrieve_flight_info():
  token = get_opensky_token()
  headers = {"Authorization": f"Bearer {token}"}

  url = "https://opensky-network.org/api/states/all"
  r = requests.get(url, headers=headers)
  r.raise_for_status()
  states = r.json()
  stateData = states.get('states')
  flightData = []
  for s in stateData:
    if (s[2] == "United States") and (("DAL" in s[1]) or ("AAL" in s[1]) or ("UAL" in s[1])):
        flightData.append({'icao24': s[0],
                            'callsign': s[1],
                            'origin_country': s[2],
                            'longitude': s[5],
                            'latitude': s[6],
                            'baro_altitude': s[7],
                            'on_ground': s[8],
                            'velocity': s[9],
                            'true_track': s[10],
                            'geo_altitude': s[13]
                            })
  return flightData


@app.get("/get_trajectory/{icao24}")
def get_trajectory(icao24):
    token = get_opensky_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = f"https://opensky-network.org/api/tracks/all?icao24={icao24}&time=0"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    trajectory_data = r.json()
    if (trajectory_data):
        path_dict = []
        for p in trajectory_data.get("path", []):
            path_dict.append({
                "time": p[0],
                "latitude": p[1],
                "longitude": p[2],
                "altitude": p[3],
                "heading": p[4],
                "on_ground": p[5]
            })
        return path_dict
    else:
        print("error finding trajectory data")

@app.get("/weather/{layer}/{z}/{x}/{y}.png")
def get_weather_layer(layer, z, x, y):
    url = f"https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API_KEY}"
    resp = requests.get(url)
    resp.raise_for_status()
    return Response(resp.content, media_type = "image/png")

    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "static"), html=True), name="static")