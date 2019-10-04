from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request, urlopen
import json


class WeatherDevice(DddDevice):

    def getData(self, city, country, unit="metric"):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=%s&APPID=d258b72f49da373d5ee9a33f525d1252' % (city,country,unit)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class temperature(DeviceWHQuery):
        def perform(self, city, country, unit):
            data = self.device.getData(city, country, unit)
            temp = data['main']['temp']
            tempstr = str(temp)
            return [tempstr]

    class weather(DeviceWHQuery):
        def perform(self, city,country):
            data = self.device.getData(city, country)
            weather = data['weather'][0]['description']
            weatherstr = str(weather)
            return [weatherstr]
