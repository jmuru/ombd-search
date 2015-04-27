import json
import bisect as b
import csv
from operator import itemgetter
import urllib
from urllib2 import urlopen

url_start = 'http://www.omdbapi.com/?'

def searchUrl(title, year):
	s_params = {
	't': title,
	'y': year
	}
	url_suffix = urllib.urlencode(s_params)
	final_url = url_start + url_suffix
	return request(final_url)

def request(url):
	mov_data = json.loads(urlopen(url).read())
	if mov_data['Plot'] == "N/A":
		return "this movie does not have a plot"
	return mov_data['Title'] + ' : ' + mov_data['Plot']

print(searchUrl("cow", "2009"))