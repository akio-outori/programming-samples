#!/usr/bin/python

import os
import cgi
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
				autoescape = True )

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		print params
#		params = self.__escape(params)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

#	def __escape(self, **params):
#		return cgi.escape(params)

class MainPage(Handler):
	def get(self):
		self.render("index.html")

class ShoppingList(Handler):
	def get(self):
		items = self.request.get_all("food")
		self.render("shopping_list.html", items = items)

class FizzBuzz(Handler):
	def get(self):
		n = self.request.get("number")
		try:
			self.render("fizzbuzz.html", number = int(n))
		except:
			self.render("fizzbuzz.html")

app = webapp2.WSGIApplication([('/', MainPage),
				('/shopping_list', ShoppingList),
				('/fizzbuzz', FizzBuzz)
					],
					debug = True)
