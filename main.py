import requests

API_Key = "1916d150df13c5197c107e364a08863b"
#MY_LAT = 59.2928
#MY_LONG = 15.2151
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 43.36
MY_LONG = 3.52

params = {
    "lat": MY_LAT,
    "lon":MY_LONG,
    "appid": API_Key,
    "units": "metric",
    "exclude": "current,daily,minutely",
}

def umbrella():

    api = requests.get(OWM_Endpoint, params=params)
    api.raise_for_status()

    weather = api.json()

    hourly_weather = weather["hourly"]


    for i in range(0, 12):
        if int(hourly_weather[i]["weather"][0]["id"]) < 600:
            return True



print(umbrella())




