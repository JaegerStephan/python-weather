# import the module
import python_weather
import asyncio

# declare the client. format defaults to metric system (celcius, km/h, etc.)
client = python_weather.Client(format=python_weather.METRIC)

# add loop
loop = asyncio.get_event_loop()

# fetch a weather forecast from a city
weather = loop.run_until_complete(client.find("Osterhofen"))

# returns the current city temperature (int)
print(weather.current.temperature)

# get the weather forecast for a few days
for forecast in weather.forecast:
    print(str(forecast.date), forecast.sky_text, forecast.sky_code_day, forecast.temperature, 
            forecast.low, forecast.high, forecast.precipitation)

