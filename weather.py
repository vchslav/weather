#pyowm 3.2.0 https://pypi.org/project/pyowm/

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def get_curr_temp():

    owm = OWM('7045f4addca69a18ddabc4c10d413d8a')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Tel-Aviv,IL')
    w = observation.weather
    temp = w.temperature('celsius')
    return temp


if __name__ == '__main__':
    curr_temp = get_curr_temp()
    print("Hello, Iguazio")
    print("Temperature in Tel-Aviv:", curr_temp)


