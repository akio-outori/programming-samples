# Classes used to help generate content for the My Movie Website page.
# very similar to the class example, as these only define instance variables
# that are used for content generation later.
#
# Movie Ratings are also supported, but not utilized in the code currently.
# 

class Video():
	"""Parent class for media of all types.
	Provides .title and .description for all titles."""
	def __init__(self, title, description):
		self.title		= title
		self.description	= description

class Movie(Video):
	"""Class that provides a way to store movie related information.
	Calls Video() to provide .title and .description as well as adding
	functionality for .runtime, .poster_image_url, and .trailer_youtube_url."""
	valid_ratings = ["G", "PG", "PG-13", "R"]
	def __init__(self, title, runtime, description, poster_image, trailer_youtube):
		Video.__init__(self, title, description)
		self.runtime			= runtime
		self.poster_image_url		= poster_image
		self.trailer_youtube_url	= trailer_youtube

class TVShow(Video):
	"""Class that provides a way to store TV Show related information.
	Calls Video() to provide .title and .description as well as adding
	functionality for .episodes, .poster_image_url, and .trailer_youtube_url."""
	def __init__(self, title, episodes, description, poster_image, trailer_youtube):
		Video.__init__(self, title, description)
		self.episodes			= episodes
		self.poster_image_url		= poster_image
		self.trailer_youtube_url	= trailer_youtube
