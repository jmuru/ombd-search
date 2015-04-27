import json
import bisect as b
import csv
from operator import itemgetter
import urllib
from urllib2 import urlopen

ratingList = []
titleList = []

with open('movies.csv') as f:
	read_file = csv.reader(f)


	for row in read_file:
		lines.append(row)
	for row in lines:
		url_start = 'http://www.omdbapi.com/?'
		s_params = {
			't': row[0],
			'y': row[1]
		}
		url_pre = urllib.urlencode(s_params)
		# create search url
		search_url = url_start + url_pre

		# Show json representation of each ombd object
		imdbData = json.loads(urlopen(search_url).read())
		
		# handling corner cases: if movie not found return -2, if movie found but no rating return -1
		if imdbData['Response'] == 'False':

			imdbData['Title'] = 'Movie not Found'

			rating = -2

		elif imdbData['imdbRating'] == "N/A":

			rating = -1

		else:

			rating = float(imdbData['imdbRating'])

		# sort movie indexes
		order_ratings = b.bisect_left(ratingList, rating )

		# insert movie rating by index order
		ratingList.insert(order_ratings, rating)

		# insert movie title by index order
		titleList.insert(order_ratings, (imdbData['Title']))
# combine title and rating list		
mov_tuple_list = zip(titleList, ratingList)


# format: movie - rating
for (title, rating) in reversed(mov_tuple_list):

	print(title.encode('utf8') + ' - ' + str(rating))

