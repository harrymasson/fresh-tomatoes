"""This script creates list of movies with data and then
launches 'Fresh Tomatoes' movie rating website."""

from media import Movie
import fresh_tomatoes

def main():
    """Function called when executed as standalone script"""
    movies = []
    #Add "Toy Story"
    toy_story = Movie("Toy Story",
                      "http://blog.nileslibrary.org/assets/toystory.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                      1995,
                      4.2
                     )

    movies.append(toy_story)

    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
