import requests
from twilio.rest import Client

API_Key = "1916d150df13c5197c107e364a08863b"
MY_LAT = 59.2928
MY_LONG = 15.2151
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"

account_sid =''
auth_token = ''
to_number = ''
from_number = ''

params = {
    "lat": MY_LAT,
    "lon":MY_LONG,
    "appid": API_Key,
    "units": "metric",
    "exclude": "current,daily,minutely",
}

api = requests.get(OWM_Endpoint, params=params)
api.raise_for_status()

weather = api.json()

hourly_weather = weather["hourly"]
weather_slice = hourly_weather[:12]

will_rain = False


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True




if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="It will rain today.",
                         from_='',
                         to=''
                     )





