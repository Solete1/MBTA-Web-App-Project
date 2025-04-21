import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_TOKEN = os.getenv("MBTA_API_KEY")

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_lat_long(place_name):
    print("🔎 Getting lat/long for:", place_name)

    encoded_place = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{encoded_place}.json?access_token={MAPBOX_TOKEN}&types=poi"
    print("📡 Mapbox URL:", url)

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            coords = data["features"][0]["geometry"]["coordinates"]
            latitude, longitude = coords[1], coords[0]
            print(f"📍 Coordinates for '{place_name}': ({latitude}, {longitude})")
            return latitude, longitude
    except Exception as e:
        print("❌ Error getting lat/long:", e)
        raise

def get_nearest_station(latitude, longitude):
    print(f"🚇 Getting nearest MBTA stop for coordinates: ({latitude}, {longitude})")

    url = (
        f"{MBTA_BASE_URL}?api_key={MBTA_TOKEN}"
        f"&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    )
    print("📡 MBTA URL:", url)

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            stop = data["data"][0]
            stop_name = stop["attributes"]["name"]
            wheelchair = stop["attributes"]["wheelchair_boarding"]
            wheelchair_access = (
                "Yes" if wheelchair == 1 else "No" if wheelchair == 2 else "Unknown"
            )
            print(f"✅ Nearest stop: {stop_name} (Wheelchair Accessible: {wheelchair_access})")
            return stop_name, wheelchair_access
    except Exception as e:
        print("❌ Error getting nearest station:", e)
        raise

def find_stop_near(place_name):
    print(f"Looking up: {place_name}")
    lat, lon = get_lat_long(place_name)
    print(f"Coordinates: {lat}, {lon}")
    stop, wheelchair = get_nearest_station(lat, lon)
    print(f"Stop: {stop}, Wheelchair Accessible: {wheelchair}")
    return stop, wheelchair
