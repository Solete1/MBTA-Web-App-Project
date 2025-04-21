import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_lat_long(place_name):
    query = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        coords = data["features"][0]["geometry"]["coordinates"]
        return coords[1], coords[0]  # (lat, lon)

def get_nearest_station(latitude, longitude):
    url = (f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}" 
           f"&filter[longitude]={longitude}&sort=distance")
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        stop = data["data"][0]
        stop_name = stop["attributes"]["name"]
        wheelchair = stop["attributes"]["wheelchair_boarding"]
        wheelchair_access = "Yes" if wheelchair == 1 else "No" if wheelchair == 2 else "Unknown"
        return stop_name, wheelchair_access

def find_stop_near(place_name):
    lat, lon = get_lat_long(place_name)
    return get_nearest_station(lat, lon)