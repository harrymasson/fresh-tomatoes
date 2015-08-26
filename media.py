"""This module contains Movie class"""

import re

class Movie(object):
    """Class to encapsulate Movie data for display in HTML page"""
    def __init__(self, title, poster_image_url, trailer_youtube_url, release_year, rating):
        """Initialization method for Movie class"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year
        self.set_rating(rating)

    def set_rating(self, rating):
        """Method that enforces rating limits (ensures rating is between 0 and 5, and rounds
           rating (to nearest whole number, then sets adjusted rating to instance variable"""
        if rating < 0:
            self.rating = 0
        elif rating > 5:
            self.rating = 5
        else:
            self.rating = int(round(rating))

    def get_youtube_id(self):
        """Method that extracts and returns the youtube ID from the url"""
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        return trailer_youtube_id
