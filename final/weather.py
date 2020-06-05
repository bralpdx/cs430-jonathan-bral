import os
import json
import requests
import geocoder

API_KEY = os.environ['OPEN_KEY']

def convert_fahr(temp):
    '''
    Converts form Kelvin to Fahrenheit
    '''
    result = (temp - 273.15) * (1.8) + 32
    return round(result)

def get_weather():
    '''
    Gets latitude and longitude
    based off of user IP address
    via geocoder API
    '''
    g = geocoder.ip('me')
    lat = str(g.lat)
    lon = str(g.lng)

    '''
    OpenWeather API retrieves locational
    weather data.
    '''
    url = 'http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid='+API_KEY
    res = requests.get(url)
    data = res.json()
    report = { 
            "conditions": str(data['weather'][0]['description']),
            "temp": str(convert_fahr(data['main']['temp']))
        }
    

    return report
