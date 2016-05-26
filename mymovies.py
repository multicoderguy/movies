import media
import fresh_tomatoes

holy_grail = media.Movie("Quest for the Hold Grail",
                         "King Arthur searches for the Holy Grail.",
                         "http://www.movie-list.com/img/posters/big/zoom/montypythonandtheholygrail.jpg",
                         "https://www.youtube.com/watch?v=LG1PlkURjxE")

freddy_got_f = media.Movie("Freddy Got Fingered",
                           "Gordy, and animator, leaves home to fulfill his dreams.",
                           "http://images.moviepostershop.com//freddy-got-fingered-movie-poster-1020476187.jpg",
                           "http://www.youtube.com/watch?v=OwoVgMEXusM")

austin_powers = media.Movie("Austin Powers: International Man of Mystery",
                           "The international man of mystery fights the ultimate Dr. Evil",
                           "http://static.rogerebert.com/uploads/movie/movie_poster/austin-powers-international-man-of-mystery-1997/large_mLVymsqdkwNNKjw2ZXn8fkor3om.jpg",
                           "http://www.youtube.com/watch?v=_tQMdNoc8T8")

movies = [freddy_got_f,holy_grail,austin_powers]
fresh_tomatoes.open_movies_page(movies)

