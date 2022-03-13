import requests

API_Key = "1916d150df13c5197c107e364a08863b"
MY_LAT = 59.2928
MY_LONG = 15.2151
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": MY_LAT,
    "lon":MY_LONG,
    "appid": API_Key,
    "units": "metric"
}



api = requests.get(OWM_Endpoint, params=params)

weather = api.json()

hourly_weather = weather["hourly"]

print(hourly_weather)


