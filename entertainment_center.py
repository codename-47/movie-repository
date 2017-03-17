import fresh_tomatoes
import media

taken = media.Movie('Taken', 
	'An action thriller where a father saves his daughter.', 
	'https://www.cinematerial.com/media/posters/md/ls/ls2bswa5.jpg?v=1456295186', 
	'https://www.youtube.com/watch?v=3Tz9tQr1Zgo')

hunger_games = media.Movie('The Hunger Games', 
	'Katnis goes into the Hunger games and changes the rules.',
	'https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg', 
	'https://www.youtube.com/watch?v=4S9a5V9ODuY')

movies = [taken, hunger_games]
fresh_tomatoes.open_movies_page(movies)