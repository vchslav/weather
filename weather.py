import pyowm

APIKEY='7045f4addca69a18ddabc4c10d413d8a' 
owm = pyowm.OWM(APIKEY) # TODO: Replace <api_key> with your API key
la = owm.three_hours_forecast('Los Angeles, US')
print(la.will_have_clouds())
