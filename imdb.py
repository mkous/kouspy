import requests
import sys

help = "usage: imdb.py [name of the movie]"

if len(sys.argv) < 2:
    print help
else:
    title = sys.argv[1]
    uri = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'
    r = requests.get(uri.format(title))

    print "IMDB score: " + r.json()['imdbRating']
    print r.json()['Awards']
