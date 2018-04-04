import fresh_tomatoes
import media


'''Creating a Movie object for toy_story'''
toy_story = media.Movie(
    "Toy Story",
    "Toys Come to Life",
    "toy_story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

'''Creating a Movie object for avatar'''
avatar = media.Movie(
    "Avatar",
    "Life on an alien planet",
    "avatar.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

'''Creating a Movie object for avengers_infinity_war'''
avengers_infinity_war = media.Movie(
    "Avengers Infinity War",
    "Time is running out",
    "infinity_war.jpg",
    "https://www.youtube.com/watch?v=QwievZ1Tx-8&t=2s")

'''Creating a Movie object for school_of_rock'''
school_of_rock = media.Movie(
    "School of Rock",
    "A new teacher is in town",
    "school_of_rock.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

'''Creating a Movie object for ratatouille'''
ratatouille = media.Movie(
    "Ratatouille",
    "Big dreams start small",
    "ratatouille.jpg",
    "https://www.youtube.com/watch?v=1yKqLNnxGZw")

'''Creating a Movie object for the_hunger_games'''
the_hunger_games = media.Movie(
    "The Hunger Games",
    "A fight for the future",
    "hunger_games.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

'''Creating a list of movie object names '''
movies = [toy_story, avatar, avengers_infinity_war,
          school_of_rock, ratatouille, the_hunger_games]

'''Calling open_movies from fresh_tomatoes and passing the list movies
as a parameter'''
fresh_tomatoes.open_movies_page(movies)
