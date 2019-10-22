from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request, urlopen
import json


class WeatherDevice(DddDevice):

    def clean_query(self, query):
        query = query.replace(' ', '+')
        return query

    def has_content(self, data):
        if data["Response"] == "True":
            return True
        else:
            return False

    def getData(self, title, extent="short", production_type="", year=""):

        #Default for type is movie but doesn't need to be specified

        apikey='37ea90c2'
        url = 'http://www.omdbapi.com/?t=%s&plot=%s&type=%s&y=%s&apikey=%s' % (title,extent,production_type,year,apikey)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class actors(DeviceWHQuery):
        def perform(self, title, production_type):
            title = self.device.clean_query(title)
            data = self.device.getData(title, "", production_type, "")

            if self.device.has_content(data):
                actors = data["Actors"]
                answer = str(actors)
            else:
                answer = 'None (no such title)'

            return [answer]

    class release(DeviceWHQuery):
        def perform(self, title):
            title = self.device.clean_query(title)
            data = self.device.getData(title)

            if self.device.has_content(data):
                year = data["Year"]
                answer = str(year)
            else:
                answer = 'None (no such title)'

            return [answer]

    class plot(DeviceWHQuery):
        def perform(self, title, extent):
            title = self.device.clean_query(title)
            extent = extent.split()[0]
            data = self.device.getData(title, extent, "", "")

            if self.device.has_content(data):
                plot = data["Plot"]
                answer = str(plot)
            else:
                answer = 'None (no such title)'

            return [answer]

    class genre(DeviceWHQuery):
        def perform(self, title):
            title = self.device.clean_query(title)
            data = self.device.getData(title)

            if self.device.has_content(data):
                genre = data["Genre"]
                answer = str(genre)
            else:
                answer = 'None (no such title)'

            return [answer]

    class ratings(DeviceWHQuery):
        def perform(self, title):
            title = self.device.clean_query(title)
            data = self.device.getData(title)

            if self.device.has_content(data):
                ratings = data["imbdRating"]
                answer = str(ratings)
            else:
                answer = 'None (no such title)'

            return [answer]
