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

    class results(DeviceWHQuery):
        def perform(self, query):

            all_answers = []

            movie_data = self.device.getData(query, "", production_type="movie", year="")
            series_data = self.device.getData(query, "", production_type="series", year="")
            episode_data = self.device.getData(query, "", production_type="episode", year="")

            if movie_data["Response"] == "True":
                movie_str = "%s, %s from %s" % (movie_data["Title"], movie_data["Type"], movie_data["Year"])
                all_answers.append(movie_str)

            if series_data["Response"] == "True":
                series_str = "%s, %s from %s" % (series_data["Title"], series_data["Type"], series_data["Year"])
                all_answers.append(series_str)

            if episode_data["Response"] == "True":
                episode_str = "%s, %s from %s" % (episode_data["Title"], episode_data["Type"], episode_data["Year"])
                all_answers.append(episode_str)

            all_string = " ".join(all_answers)

            return [all_string]
