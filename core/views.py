import json
from django.http import HttpResponse
from django.shortcuts import render

from core.open_weather_map import search_by_city
from core.models import CityOpenWeatherMap


def index(request):
    data = {}
    if request.method == "POST":
        city = request.POST["the_post"] if "the_post" in request.POST else ""
        if city == "":
            return HttpResponse()

        city_weather = search_by_city(city)[1]
        data = city_weather["weather"] if "weather" in city_weather else ""
        weather, created = CityOpenWeatherMap.objects.get_or_create(
            name=city, weather_data=data
        )
        if created:
            print("created")
        return HttpResponse(json.dumps(weather.weather_data))

    if request.method == "GET":
        the_post = (
            request.GET["fetch_city_weather"]
            if "fetch_city_weather" in request.GET
            else ""
        )
        if the_post == "weather":
            _data = CityOpenWeatherMap.objects.all().order_by("-date_created")
            return HttpResponse(_data)

    return render(request, "core/index.html", data)
