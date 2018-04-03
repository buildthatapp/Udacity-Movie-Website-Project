import fresh_tomatoes
import media

toy_story = media.Movie(
	"Toy Story",
    "Toys Come to Life",
	"toy_story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
	"Avatar",
	"Life on an alien planet",
	"avatar.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

avengers_infinity_war = media.Movie(
	"Avengers Infinity War",
	"Time is running out",
	"infinity_war.jpg",
	"https://www.youtube.com/watch?v=QwievZ1Tx-8&t=2s")

school_of_rock = media.Movie(
	"School of Rock",
	"A new teacher is in town",
	"school_of_rock.jpg",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie(
	"Ratatouille",
	"Big dreams start small",
	"ratatouille.jpg",
	"https://www.youtube.com/watch?v=1yKqLNnxGZw")

the_hunger_games = media.Movie(
	"The Hunger Games",
	"A fight for the future",
	"hunger_games.jpg",
	"https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, avengers_infinity_war,
	school_of_rock, ratatouille, the_hunger_games]

fresh_tomatoes.open_movies_page(movies)
