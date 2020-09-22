from django.forms import ModelForm

from meteoserver.api.models import WeatherRecord

FIELD_MAP = {
    'stationtype': 'station_type',
    'dateutc': 'date',
    'tempinf': 'temp_in',
    'humidityin': 'humidity_in',
    'baromrelin': 'pressure_rel',
    'baromabsin': 'pressure_abs',
    'tempf': 'temp_out',
    'humidity': 'humidity_out',
    'winddir': 'wind_dir',
    'windspeedmph': 'wind_speed',
    'windgustmph': 'wind_gust',
    'maxdailygust': 'wind_max_daily_gust',
    'rainratein': 'rain_rate',
    'eventrainin': 'rain_event',
    'hourlyrainin': 'rain_hourly',
    'dailyrainin': 'rain_daily',
    'weeklyrainin': 'rain_weekly',
    'monthlyrainin': 'rain_monthly',
    'totalrainin': 'rain_total',
    'solarradiation': 'solar_radiation',
    'uv': 'uv_index'
    }


def fahrenheit_to_centigrade(value):
    return round((value - 32.0) / 1.8, 2)


def mph_to_kmh(value):
    return round(value * 1.609344, 2)


def in_to_hpa(value):
    return round(value * 33.86389, 2)


def in_to_mm(value):
    return round(value * 25.4, 2)


class WeatherForm(ModelForm):
    class Meta:
        model = WeatherRecord
        fields = '__all__'

    def clean_pressure_abs(self):
        val = self.cleaned_data['pressure_abs']
        return in_to_hpa(val)

    def clean_pressure_rel(self):
        val = self.cleaned_data['pressure_rel']
        return in_to_hpa(val)

    def clean_rain_daily(self):
        val = self.cleaned_data['rain_daily']
        return in_to_mm(val)

    def clean_rain_event(self):
        val = self.cleaned_data['rain_event']
        return in_to_mm(val)

    def clean_rain_hourly(self):
        val = self.cleaned_data['rain_hourly']
        return in_to_mm(val)

    def clean_rain_monthly(self):
        val = self.cleaned_data['rain_monthly']
        return in_to_mm(val)

    def clean_rain_rate(self):
        val = self.cleaned_data['rain_rate']
        return in_to_mm(val)

    def clean_rain_total(self):
        val = self.cleaned_data['rain_total']
        return in_to_mm(val)

    def clean_rain_weekly(self):
        val = self.cleaned_data['rain_weekly']
        return in_to_mm(val)

    def clean_temp_in(self):
        val = self.cleaned_data['temp_in']
        return fahrenheit_to_centigrade(val)

    def clean_temp_out(self):
        val = self.cleaned_data['temp_out']
        return fahrenheit_to_centigrade(val)

    def clean_wind_gust(self):
        val = self.cleaned_data['wind_gust']
        return mph_to_kmh(val)

    def clean_wind_max_daily_gust(self):
        val = self.cleaned_data['wind_max_daily_gust']
        return mph_to_kmh(val)

    def clean_wind_speed(self):
        val = self.cleaned_data['wind_speed']
        return mph_to_kmh(val)
