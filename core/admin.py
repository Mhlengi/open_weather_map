from django.contrib import admin
from core.models import CityOpenWeatherMap


class CityOpenWeatherMapAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "weather_data",
        "has_weather_data",
        "date_created",
    )


admin.site.register(CityOpenWeatherMap, CityOpenWeatherMapAdmin)
