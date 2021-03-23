import pyowm # import Python Open Weather Map to our project.

APIKEY='7045f4addca69a18ddabc4c10d413d8a'                  #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
mng = OpenWMap.weather_manager()    #NEW
obs = mng.weather_at_place('Tel-Aviv')
#Weather=OpenWMap.weather_at_place(Tel-Aviv)  # give where you need to see the weather
#Data=Weather.get_weather()                 # get out data in the mentioned location
NewData=obs.get_weather()  
temp=NewData.get_temperature(unit='celsius') #NEW
print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
