import json
import requests
import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    topArtists = json.loads(data)
    topArtist = topArtists['topartists']['artist'][0]['name']
    return topArtist # return the top artist in Spain

url = 'http://ws.audioscrobbler.com/2.0/?method=geo.getTopArtists&api_key=51de025812af79cb70f4a872936181a0&country=Spain&limit=1&format=json'
print api_get_request(url)
