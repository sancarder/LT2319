from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request, urlopen
import json

GREYS = "show_greys_anatomy"
FRIENDS = "show_friends"
HOMELAND = "show_homeland"

SHOWS = {
    "grey's anatomy": GREYS,
    "friends": FRIENDS,
    "homeland": HOMELAND,
}

class FilmophileDevice(DddDevice):

    def clean_query(self, query):
        query = query.replace(' ', '+')
        return query

    def clean_number(self, query):
        words_to_numbers = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10'}

        nr = query.split()[1]

        if nr.isdigit():
            number = nr
        else:
            number = words_to_numbers[nr]
        
        return number

    def has_content(self, data):
        if data["Response"] == "True":
            return True
        else:
            return False

    def getData(self, title, extent="short", production_type="", season="", episode=""):

        #Default for type is movie but doesn't need to be specified

        apikey='37ea90c2'
        url = 'http://www.omdbapi.com/?t=%s&plot=%s&type=%s&season=%s&episode=%s&apikey=%s' % (title,extent,production_type,season,episode,apikey)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class actors(DeviceWHQuery):
        def perform(self, title, production_type):
            title = self.device.clean_query(title)
            data = self.device.getData(title, "", production_type)

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
            data = self.device.getData(title, extent, "")

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
                ratings = data["imdbRating"]
                answer = str(ratings)
            else:
                answer = 'None (no such title)'

            return [answer]

    class episode_ratings(DeviceWHQuery):
        def perform(self, title, season, episode):
            title = self.device.clean_query(title)
            season = self.device.clean_number(season)
            episode = self.device.clean_number(episode)
            data = self.device.getData(title, "", "", season, episode)

            if self.device.has_content(data):
                ratings = data["imdbRating"]
                answer = str(ratings)
            else:
                answer = 'None (no such title)'

            return [answer]

    class episode_director(DeviceWHQuery):
        def perform(self, show, season, episode):
            show = self.device.clean_query(show)
            season = self.device.clean_number(season)
            episode = self.device.clean_number(episode)
            data = self.device.getData(show, "", "", season, episode)

            if self.device.has_content(data):
                director = data["Director"]
                answer = str(director)
            else:
                answer = 'None (no such title)'

            return [answer]

    class episode_plot(DeviceWHQuery):
        def perform(self, title, season, episode, extent):

            title = self.device.clean_query(title)
            season = self.device.clean_number(season)
            episode = self.device.clean_number(episode)
            extent = extent.split()[0]
            data = self.device.getData(title, extent, "", season, episode)

            if self.device.has_content(data):
                plot = data["Plot"]
                answer = str(plot)
            else:
                answer = 'None (no such title)'

            return [answer]

    class episode_title(DeviceWHQuery):
        def perform(self, show, season, episode):

            show = self.device.clean_query(show)
            season = self.device.clean_number(season)
            episode = self.device.clean_number(episode)
            data = self.device.getData(show, "", "", season, episode)

            if self.device.has_content(data):
                title = data["Title"]
                answer = str(title)
            else:
                answer = 'None (no such title)'

            return [answer]

    class show_to_search(DeviceWHQuery):
        def perform(self):
            options = [SHOWS[i] for i in SHOWS.keys()]
            return options
