from functions import *
import requests #Allows to send requests to API

API_KEY = "69a871b96321484cf5e4b02594207937"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" 

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url) #store info assocaited with city

#Check for successful response
if response.status_code == 200:
    data = response.json() 
    print(data)
    #Weather
    weather = weather(data)
    #Temperature
    temperature, maxTemperature, minTemperature, feelsLike = temperature(data)
    #Wind
    windSpeed = windSpeed(data)
    #Print
    printWeather(weather, temperature, maxTemperature, minTemperature, feelsLike, windSpeed)
else:
    print("An error has occurred.")





