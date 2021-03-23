from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('7045f4addca69a18ddabc4c10d413d8a')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Tel-Aviv,IL')
w = observation.weather

for i in w:

print(w.temperature('celsius'))

