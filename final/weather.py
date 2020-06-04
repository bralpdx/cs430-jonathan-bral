import os
import json
import requests

API_KEY = os.environ['OPEN_KEY']

def convert_fahr(temp):
    '''
    Converts form Kelvin to Fahrenheit
    '''
    result = (temp - 273.15) * (1.8) + 32
    return round(result)

def get_weather():
    lat = '45.5977'
    lon = '-123.0008'
    url = 'http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid='+API_KEY
    res = requests.get(url)
    data = res.json()
    report = { 
            "conditions": str(data['weather'][0]['description']),
            "temp": str(convert_fahr(data['main']['temp']))
        }
    

    return report
