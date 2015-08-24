#entertainment_center.py
import Movie from media
import fresh_tomatoes

movies = []

toy_story = media.Movie(
		"Toy Story",
		"http://blog.nileslibrary.org/assets/toystory.jpg",
		"https://www.youtube.com/watch?v=KYz2wyBy3kc"
	)
movies.append(toy_story)

fresh_tomatoes.open_movies_page(movies)