import pyowm
owm = pyowm.OWM('<api_key>') # TODO: Replace <api_key> with your API key
la = owm.three_hours_forecast('Los Angeles, US')
print(la.will_have_clouds())
