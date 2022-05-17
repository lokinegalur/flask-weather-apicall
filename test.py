import requests
import json

city = "Bangalore"
country = "IND"

api_key = "##"

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

weather_data = weather_url.json()
print(weather_data)
temp=round(weather_data['main']['temp'])
humidity=weather_data['main']['humidity']
wind_speed=weather_data['wind']['speed']
#print(weather_data,temp,humidity,wind_speed,sep='\n')