from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request, urlopen
import json


class AskImdbDevice(DddDevice):

    def getData(self, movie):
        apikey = '37ea90c2'
        url = 'http://www.omdbapi.com/?t=%s&apikey=%s' % (movie, apikey)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)


    class find_actors(DeviceWHQuery):
        def perform(self, movie):
            data = self.device.getData(movie)
            print("Data: %s" % (data))
            query = unicode("Actors")
            print("Query: %s" % (query))
            temp = data[query]
            print("Temp: %s" % (temp))
            actors = str(temp)
            print("Actors: %s" % (actors))
            return [actors]

    class find_year(DeviceWHQuery):
        def perform(self, movie):
            data = self.device.getData(movie)
            print("Data: %s" % (data))
            query = unicode("Year")
            print("Query: %s" % (query))
            temp = data[query]
            print("Temp: %s" % (temp))
            year = str(temp)
            print("Year: %s" % (actors))
            return [year]
