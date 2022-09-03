def weather(data):
    weather = data['weather'][0]['description']
    return weather

def temperature(data):
    temperature = data['main']['temp']
    maxTemperature = data['main']['temp_max']
    minTemperature = data['main']['temp_min']
    feelsLike = data['main']['feels_like']
    return temperature, maxTemperature, minTemperature, feelsLike

def windSpeed(data):
    windSpeed = data['wind']['speed']
    return windSpeed

def printWeather(weather, temperature, maxTemperature, minTemperature, feelsLike, windSpeed):
    print("------------------------------")
    print("-------WEATHER FORECAST-------")
    print("------------------------------")
    print("        -         ")
    print("Cloud coverage:", weather)
    print("        -         ")
    print("Maximum temperature: {:.0f} degree celsius".format(maxTemperature - 273.15))
    print("Average temperature: {:.0f} degree celsius".format(temperature - 273.15))
    print("Minimum temperature: {:.0f} degree celsius".format(minTemperature - 273.15))
    print("Feels like: {:.0f} degree celsius".format(feelsLike - 273.15))
    print("        -         ")
    print("Wind speed: {:.2f} mph".format(windSpeed))