from django.db import models

# Create your models here.
"""
EXAMPLE POST DATA
{
    'PASSKEY': ['435260D782612391975E850CE8F25347'],
    'stationtype': ['EasyWeatherV1.5.0'],
    'dateutc': ['2020-05-30 09:13:24'],
    'tempinf': ['71.6'],
    'humidityin': ['64'],
    'baromrelin': ['29.968'],
    'baromabsin': ['29.983'],
    'tempf': ['73.8'],
    'humidity': ['67'],
    'winddir': ['151'],
    'windspeedmph': ['1.3'],
    'windgustmph': ['2.2'],
    'maxdailygust': ['13.6'],
    'rainratein': ['0.000'],
    'eventrainin': ['0.000'],
    'hourlyrainin': ['0.000'],
    'dailyrainin': ['0.000'],
    'weeklyrainin': ['0.000'],
    'monthlyrainin': ['1.130'],
    'totalrainin': ['10.240'],
    'solarradiation': ['638.47'],
    'uv': ['6'],
    'model': ['WS2900']
}
"""


class WeatherRecord(models.Model):
    date = models.DateTimeField()
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    humidity_in = models.FloatField()
    humidity_out = models.FloatField()
    pressure_abs = models.FloatField()
    pressure_rel = models.FloatField()
    wind_dir = models.FloatField()
    wind_speed = models.FloatField()
    wind_gust = models.FloatField()
    wind_max_daily_gust = models.FloatField()
    rain_rate = models.FloatField()
    rain_event = models.FloatField()
    rain_hourly = models.FloatField()
    rain_daily = models.FloatField()
    rain_weekly = models.FloatField()
    rain_monthly = models.FloatField()
    rain_total = models.FloatField()
    solar_radiation = models.FloatField()
    uv_index = models.FloatField()
    station_type = models.CharField(max_length=50)
