from pyowm import OWM

APIKEY='7045f4addca69a18ddabc4c10d413d8a' 
owm = OWM(APIKEY) # TODO: Replace <api_key> with your API key
mgr = owm.weather_manager()
observation = mgr.weather_at_place('San Francisco, US')
weather = observation.get_weather()
print(weather.get_temperature('fahrenheit')['temp'])

