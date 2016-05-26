import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life.",
                        "http://www.dvdsreleasedates.com/posters/800/T/Toy-Story-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://fanaru.com/avatar/image/6676-avatar-avatar-movie-poster.jpg",
                     "http://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)
avatar.show_trailer()
