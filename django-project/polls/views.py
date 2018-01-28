# This file defines the "views" for /polls.  This could be any valid HTTP content
# As long as it returns a valid HTTP response.  Each page/directory is dealt with as
# a method.

from django.shortcuts import render
from django.http import HttpResponse, Http404

# Method to search for static content and return the result.  If the content 
# doesn't exist this returns a 404 error instead.
def http_request(html_file):
	try:
		with open(html_file, 'r') as current_file:
			html=current_file.read()
		return HttpResponse(html)
	except:
		raise Http404('Page not Found.')

# Method to define an HTTP response for polls/ (the index)
# Index is served from a static file.  If the file is not found
# Kick out a default HTTP404
def index(request):
	return http_request('polls/index.html')

# Method to define an HTTP reponse for polls/detail
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

# Method to define an HTTP reponse for polls/results
def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

# MEthod to define an HTTP response for polls/vote
def vote(request, question_id):
	return HttpReponse("You're voting on question %s." % question_id)


