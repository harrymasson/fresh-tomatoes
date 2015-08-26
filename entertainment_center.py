"""This script creates list of movies with data and then
launches 'Fresh Tomatoes' movie rating website."""

from media import Movie
import fresh_tomatoes

def main():
    """Function called when executed as standalone script"""
    movies = []
    # Add each movie and respective data to list of movies
    movies.append(Movie("Toy Story",
                        "http://blog.nileslibrary.org/assets/toystory.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        1995,
                        4.2
                       )
                 )

    movies.append(Movie("Toy Story 2",
                        "http://ia.media-imdb.com/images/M/MV5BMTQ0OTU0NTcyNl5BMl5BanBnXkFtZTcwOTk5Mjc4OA@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=Lu0sotERXhI",
                        1999,
                        4.0
                       )
                 )

    movies.append(Movie("Toy Story 3",
                        "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg",
                        2010,
                        4.2
                       )
                 )

    movies.append(Movie("WALL-E",
                        "http://images1.fanpop.com/images/image_uploads/Official-Movie-Poster-wall-e-818680_565_837.jpg",
                        "https://www.youtube.com/watch?v=alIq_wG9FNk",
                        2008,
                        4.2
                       )
                 )

    movies.append(Movie("Cars",
                        "https://www.movieposter.com/posters/archive/main/98/MPW-49378w",
                        "https://www.youtube.com/watch?v=WGByijP0Leo",
                        2006,
                        3.7
                       )
                 )

    movies.append(Movie("Ratatouille",
                        "http://pixar-planet.fr/wp-content/uploads/2010/04/affiche-ratatouille-06.jpg",
                        "https://www.youtube.com/watch?v=KQUpZqshj7M",
                        2007,
                        4.0
                       )
                 )

    movies.append(Movie("Shrek",
                        "http://vignette4.wikia.nocookie.net/shrek/images/2/2a/Shrek1.jpg/revision/latest?cb=20150119043746",
                        "https://www.youtube.com/watch?v=W37DlG1i61s",
                        2001,
                        4.0
                       )
                 )

    movies.append(Movie("Shrek 2",
                        "http://vignette3.wikia.nocookie.net/voiceacting/images/1/12/Shrek_2_DVD_Cover.jpg/revision/latest?cb=20130208181328",
                        "https://www.youtube.com/watch?v=V6X5ti4YlG8",
                        2004,
                        3.6
                       )
                 )

    movies.append(Movie("Shrek the Third",
                        "http://www.gstatic.com/tv/thumb/movieposters/159731/p159731_p_v7_aa.jpg",
                        "https://www.youtube.com/watch?v=ZGmRsNM0JXM",
                        2007,
                        3.0
                       )
                 )
    # Send list of movies to be displayed via HTML
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()


