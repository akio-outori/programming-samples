#!/usr/bin/python

# Script to generate content for the Movies Website project.  Consists of two main parts:
# movies():
# Defines a list of movies (as python dictionaries, calls the media.Movie class and defines
# the content to be passed to open_movies_page()
#
# shows():
# Does exactly the same thing as movies(), but for TV shows.  Shows take slightly different
# data than movies do, and are therefore handled by different logic.  In the future this could
# almost certainly be condensed, but here the separation helps the content remain intuitive as well (I hope)
#
# Once the content is defined it is passed to the open_movies_page() method in fresh_tomatoes to generate
# the css/html.
#
# Note - one oddity here is that the text for "Description" needs to be roughly the same length
# for all defined movies or shows on the page.  If it is not, the way the tiles are organized on the 
# page can become pretty badly broken.  I've used the work-around of adding <br> statements to short
# Descriptions for now.
#



import media
import fresh_tomatoes

def movies():
	# dictionaries with the essential info for each movie to be added to the site. 
	# Each dictionary uses the following template:
	# movie		= {
	#                 'Title':
	#                 'Runtime':
	#                 'Description':
	#                 'Poster':
	#                 'Trailer':
	#		}

	blade_runner	= {
			'Title':	'Blade Runner',
			'Runtime':	'117',
			'Description':	"""A blade runner must pursue and try to terminate four replicants who stole 
					 a ship in space and have returned to Earth to find their creator.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTA4MDQxNTk2NDheQTJeQWpwZ15BbWU3MDE2NjIyODk@._V1__SX1182_SY1220_.jpg',
			'Trailer':	'https://www.youtube.com/watch?v=KPcZHjKJBnE'
		}

	transformers	= {
			'Title':	'Transformers the Movie',
			'Runtime':	'90',
			'Description':	"""The Autobots must stop a colossal planet consuming robot who goes after the Autobot Matrix of Leadership. 
					 At the same time, they must defend themselves against an all-out attack from the Decepticons.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTM2MzQ1NDA3OV5BMl5BanBnXkFtZTcwNjM2OTczMQ@@._V1__SX1182_SY1220_.jpg',
			'Trailer':	'https://www.youtube.com/watch?v=zaEWLuVJee0'
		}

	secret		= {
			'Title':	'The Secret in Their Eyes',
			'Runtime':	'129',
			'Description':	"""A retired legal counselor writes a novel hoping to find closure for one of his past unresolved homicide
					 cases and for his unreciprocated love with his superior - both of which still haunt him decades later.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTgwNTI3OTczOV5BMl5BanBnXkFtZTcwMTM3MTUyMw@@._V1__SX1182_SY1220_.jpg',
			'Trailer':	'https://www.youtube.com/watch?v=hlSASsGs73w'
		}

	martian		= {
			'Title':	'The Martian',
			'Runtime':	'144',
			'Description':	"""During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left 
					behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. 
					With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to 
					signal to Earth that he is alive.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1__SX1182_SY1220_.jpg',
			'Trailer':	'https://www.youtube.com/watch?v=ej3ioOneTy8'
		}

	star_trek	= {
			'Title':	'Star Trek VI',
			'Runtime':	'113',
			'Description':	"""On the eve of retirement, Kirk and McCoy are charged with assassinating the Klingon High Chancellor and imprisoned.
					The Enterprise crew must help them escape to thwart a conspiracy aimed at sabotaging the last best hope for peace.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTkyODE4MDIxNV5BMl5BanBnXkFtZTcwNzYxNDI4OA@@._V1__SX1182_SY1220_.jpg',
			'Trailer':	'https://www.youtube.com/watch?v=qCcf9FBsNVo'
		}

	dredd		= {
			'Title':	'Dredd',
			'Runtime':	'95',
			'Description':	"""In a violent, futuristic city where the police have the authority to act as judge, jury and executioner, a cop
					teams with a trainee to take down a gang that deals the reality-altering drug, SLO-MO.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BODkyNDQzMzUzOF5BMl5BanBnXkFtZTcwODYyMDEyOA@@._V1__SX1276_SY1220_.jpg',
			'Trailer':	'https://www.youtube.com/watch?v=G-eI5oLlIeY'
		}

	# Organize the page via positioning, so 
	# first 
	# second
	# third
	# etc

	first	= media.Movie(blade_runner['Title'], blade_runner['Runtime'], blade_runner['Description'], blade_runner['Poster'], blade_runner['Trailer'])
	second	= media.Movie(transformers['Title'], transformers['Runtime'], transformers['Description'], transformers['Poster'], transformers['Trailer']) 
	third	= media.Movie(secret['Title'], secret['Runtime'], secret['Description'], secret['Poster'], secret['Trailer'])
	fourth	= media.Movie(martian['Title'], martian['Runtime'], martian['Description'], martian['Poster'], martian['Trailer'])
	fifth	= media.Movie(star_trek['Title'], star_trek['Runtime'], star_trek['Description'], star_trek['Poster'], star_trek['Trailer'])
	sixth	= media.Movie(dredd['Title'], dredd['Runtime'], dredd['Description'], dredd['Poster'], dredd['Trailer'])

	movies = [first, second, third, fourth, fifth, sixth]
	return movies

def shows():
	# Dictionaries with the essential info for each tv show / series to be added to the site.
	# Each dictionary uses the following template:
	# series	= {
	#	'Title':
	#	'Episodes':
	#	'Description':
	#	'Poster':
	#	'Clip':
	#	}

	star_trek	= {
			'Title':	'Star Trek: The Next Generation',
			'Episodes':	'176',
			'Description':	'A new generation of Starfleet officers set off in a new Enterprise on their own mission to go where no one has gone before.',
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTgyMjY5NTg2NV5BMl5BanBnXkFtZTgwMTAzMDczMDE@._V1__SX1276_SY1220_.jpg',
			'Clip':		'https://www.youtube.com/watch?v=jtmsI07AMsE'
		}

	battlestar	= {
			'Title':	'Battlestar Galactica',
			'Episodes':	'75',
			'Description':	"""When an old enemy resurfaces and obliterate the 12 colonies, the crew of the aged Galactica 
					protect a small civilian fleet as they journey toward the fabled 13th colony, Earth.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTc1NTg1MDk3NF5BMl5BanBnXkFtZTYwNDYyMjI3._V1__SX1276_SY1220_.jpg',
			'Clip':		'https://www.youtube.com/watch?v=TnYsf2Yv8i8'
		}

	stargate	= {
			'Title':	'Stargate SG-1',
			'Episodes':	'213',
			'Description':	'A secret military team, SG-1, is formed to explore the recently discovered Stargates. <br><br>',
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTc3MjEwMTc5N15BMl5BanBnXkFtZTcwNzQ2NjQ4NA@@._V1__SX1276_SY1220_.jpg',
			'Clip':		'https://www.youtube.com/watch?v=vqOL_w4yKws'
		}

	xfiles		= {
			'Title':	'The X-Files',
			'Episodes':	'203',
			'Description':	"""Two FBI agents, Fox Mulder the believer and Dana Scully the skeptic, investigate the strange and unexplained
					while hidden forces work to impede their efforts.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BODc5MDA0MzgyOF5BMl5BanBnXkFtZTgwNjc5NjY3NzE@._V1__SX1276_SY1220_.jpg',
			'Clip':		'https://www.youtube.com/watch?v=Xcf44Nit7_A'
		}

	vikings		= {
			'Title':	'Vikings',
			'Episodes':	'29',
			'Description':	"""The world of the Vikings is brought to life through the journey of Ragnar Lothbrok, the first Viking
					to emerge from Norse legend and onto the pages of history - a man on the edge of myth.""",
			'Poster':	'http://ia.media-imdb.com/images/M/MV5BMTkyNTc3MDM4OF5BMl5BanBnXkFtZTcwODQ3NjU1OQ@@._V1__SX1276_SY1220_.jpg',
			'Clip':		'https://www.youtube.com/watch?v=1j2sXLbzm9U'
		}

	zeta_gundam	= {
			'Title':	'Zeta Gundam',
			'Episodes':	'50',
			'Description':	"""Seven years have passed since the end of the One Year War. In its zeal to stamp out any remaining opposition, 
					the Earth Federation has organized the Titans, an elite fighting force. However, the Titans soon become as oppressive
					as the former Principality of Zeon.""",
			'Poster':	'http://cdn.myanimelist.net/images/anime/4/11154l.jpg',
			'Clip':		'https://www.youtube.com/watch?v=s0sMXTDVoLc'
		}

	# Organize the page in the same way as movies, so:
	# first
	# second
	# third
	# etc
	
	first	= media.TVShow(star_trek['Title'], star_trek['Episodes'], star_trek['Description'], star_trek['Poster'], star_trek['Clip'])
	second	= media.TVShow(battlestar['Title'], battlestar['Episodes'], battlestar['Description'], battlestar['Poster'], battlestar['Clip'])
	third	= media.TVShow(stargate['Title'], stargate['Episodes'], stargate['Description'], stargate['Poster'], stargate['Clip'])
	fourth	= media.TVShow(xfiles['Title'], xfiles['Episodes'], xfiles['Description'], xfiles['Poster'], xfiles['Clip'])
	fifth	= media.TVShow(vikings['Title'], vikings['Episodes'], vikings['Description'], vikings['Poster'], vikings['Clip'])
	sixth	= media.TVShow(zeta_gundam['Title'], zeta_gundam['Episodes'], zeta_gundam['Description'], zeta_gundam['Poster'], zeta_gundam['Clip'])

	tv_shows = [first, second, third, fourth, fifth, sixth]
	return tv_shows

# Run movies() and shows() to define the content
movies	= movies()
shows	= shows()

# Call open_movies_page() to generate the page
fresh_tomatoes.open_movies_page(movies, shows)
