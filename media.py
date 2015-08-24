# media.py
import re

class Movie:
	def __init__(self,title,poster_image_url,trailer_youtube_url,release_year,rating):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.release_year = release_year
		if rating < 0:
			self.rating = 0
		elif rating > 5:
			self.rating = 5
		else:
			self.rating = int(round(rating))

	# Return Youtube Trailer ID from instance's Youtube URL.
	def get_youtube_id(self):
		# Extract the youtube ID from the url
		youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
		youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer_youtube_url)
		trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
		return trailer_youtube_id