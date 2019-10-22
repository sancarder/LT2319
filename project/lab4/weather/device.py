from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request, urlopen
import json


class WeatherDevice(DddDevice):

    def getData(self, title, extent="short", production_type="", year=""):

        #Default for type is movie but doesn't need to be specified
    
        apikey='37ea90c2'
        url = 'http://www.omdbapi.com/?t=%s&plot=%s&type=%s&y=%s&apikey=%s' % (title,extent,production_type,year,apikey)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class actors(DeviceWHQuery):
        def perform(self, title, production_type=""):
            data = self.device.getData(title, "", production_type, "")
            actors = data["Actors"]
            answer = str(actors)
            return [answer]

    class release(DeviceWHQuery):
        def perform(self, title):
            data = self.device.getData(title)
            year = data["Year"]
            answer = str(year)
            return [answer]

    class plot(DeviceWHQuery):
        def perform(self, title, extent):
            data = self.device.getData(title, extent)
            plot = data["Plot"]
            answer = str(plot)
            return [answer]

    class genre(DeviceWHQuery):
        def perform(self, title):
            data = self.device.getData(title)
            genre = data["Genre"]
            answer = str(genre)
            return [answer]

    class ratings(DeviceWHQuery):
        def perform(self, title):
            data = self.device.getData(title)
            ratings = data["imdbRating"]
            answer = str(ratings)
            return [answer]
