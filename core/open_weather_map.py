import requests

from open_weather_map.config import OPEN_WEATHER_MAP_API


def search_by_city(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
    url = "{}{}&appid={}".format(BASE_URL, city, OPEN_WEATHER_MAP_API)
    req = requests.get(url)
    return req.status_code, req.json()
