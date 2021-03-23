import pyowm

APIKEY='7045f4addca69a18ddabc4c10d413d8a' 
owm = pyowm.OWM(APIKEY) # TODO: Replace <api_key> with your API key


sf = owm.weather_at_place('San Francisco, US')
weather = sf.get_weather()
print(weather.get_temperature('fahrenheit')['temp'])
