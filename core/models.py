from django.db import models

import jsonfield


class CityOpenWeatherMap(models.Model):
    name = models.CharField(max_length=250)
    weather_data = jsonfield.JSONField()
    has_weather_data = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.name)
