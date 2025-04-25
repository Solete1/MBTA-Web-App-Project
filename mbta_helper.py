import os
import urllib.request
import json
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_TOKEN = os.getenv("MBTA_TOKEN")
OPENWEATHER_TOKEN = os.getenv("OPENWEATHER_TOKEN")  # You need to add this to your .env
TICKETMASTER_TOKEN = os.getenv("TICKETMASTER_TOKEN")  # Add this too

MAPBOX_BASE_URL = "https://api.mapbox.com/search/geocode/v6/forward"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
EVENTS_BASE_URL = "https://app.ticketmaster.com/discovery/v2/events.json"

def get_lat_long(place_name):
    encoded_place = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}?q={encoded_place}&access_token={MAPBOX_TOKEN}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        coords = data["features"][0]["geometry"]["coordinates"]
        latitude, longitude = coords[1], coords[0]
        return latitude, longitude

def get_nearest_station(latitude, longitude):
    url = (
        f"{MBTA_BASE_URL}?api_key={MBTA_TOKEN}"
        f"&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    )

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        stop = data["data"][0]
        stop_name = stop["attributes"]["name"]
        wheelchair = stop["attributes"]["wheelchair_boarding"]
        wheelchair_access = (
            "Yes" if wheelchair == 1 else "No" if wheelchair == 2 else "Unknown"
        )
        return stop_name, wheelchair_access

def get_weather(latitude, longitude):
    url = f"{WEATHER_BASE_URL}?lat={latitude}&lon={longitude}&appid={OPENWEATHER_TOKEN}&units=imperial"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        weather = {
            "description": data["weather"][0]["description"].capitalize(),
            "temperature": data["main"]["temp"]
        }
        return weather

def get_events(latitude, longitude):
    url = f"{EVENTS_BASE_URL}?apikey={TICKETMASTER_TOKEN}&latlong={latitude},{longitude}&radius=10&size=5"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            events = []
            if "_embedded" in data:
                for event in data["_embedded"]["events"]:
                    events.append(event["name"])
            return events
    except Exception:
        return ["No events found nearby."]

def find_place_info(place_name):
    lat, lon = get_lat_long(place_name)
    stop, wheelchair = get_nearest_station(lat, lon)
    weather = get_weather(lat, lon)
    events = get_events(lat, lon)
    return stop, wheelchair, weather, events
