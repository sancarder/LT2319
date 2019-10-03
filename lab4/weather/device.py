from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request, urlopen
import json


class WeatherDevice(DddDevice):


    UNITS = {
        "celsius":"metric",
        "fahrenheit":"imperial",
        "metric":"metric",
        "imperial":"imperial"
    }

    def getData(self, city, country):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=d258b72f49da373d5ee9a33f525d1252' % (city,country)
        #print url                                                                                                                                                                  
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    def getUnitData(self, city, country, unit):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=%s&APPID=d258b72f49da373d5ee9a33f525d1252' % (city,country,unit)
        #print url                                                                                                                                                                
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class temperature(DeviceWHQuery):
        def perform(self, city, country, unit):
            data = self.device.getUnitData(city, country, self.device.UNITS.get(unit))
            temp = data['main']['temp']
            print('it\'s %d degrees in %s') % (temp, city)
            tempstr = str(temp)
            return [tempstr]

    class weather(DeviceWHQuery):
        def perform(self, city,country):
            data = self.device.getData(city, country)
            weather = data['weather'][0]['description']
            print('%s in %s') % (weather, city)
            weatherstr = str(weather)
            return [weatherstr]
