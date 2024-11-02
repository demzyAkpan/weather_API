from dotenv import load_dotenv
import os
import datetime as dt
import requests

# Load environment variables from .env file
load_dotenv()


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.1
    # fahrenheit = celsius * (9/5) + 32
    return celsius



BASE_URL ="http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv('API_KEY')
CITY = "Lagos"

url = BASE_URL + "appid=" + API_KEY +"&q=" + CITY

response = requests.get(url).json()
# print(response)

wind_speed = response['wind']['speed']
temp_kelvin = response['main']['temp'] 
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']

# Extract and convert sunrise and sunset times
sunrise_timestamp = response['sys']['sunrise']
sunset_timestamp = response['sys']['sunset']
timezone_offset =response['timezone']

sunrise_time = dt.datetime.fromtimestamp(sunrise_timestamp, tz=dt.timezone.utc) + dt.timedelta(seconds=timezone_offset)
sunset_time = dt.datetime.fromtimestamp(sunset_timestamp, tz=dt.timezone.utc) + dt.timedelta(seconds=timezone_offset)

# Display weather data


print(f'temperature in {CITY}: {temp_celsius:.2f}C')
print(f'temperature in {CITY}, feels like {feels_like_celsius:.2f}')
print(f'weather in {CITY}: {description}')
print(f'Sunrise in {CITY}: {sunrise_time.strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Sunset in {CITY}: {sunset_time.strftime("%Y-%m-%d %H:%M:%S")}')

