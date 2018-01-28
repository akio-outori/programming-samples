#!/usr/bin/python

class Parent():
	"""Parent class definied as an example of inheritance."""
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last Name - " + self.last_name)
		print("Eye Color - " + self.eye_color)

class Child(Parent):
	"""Child class definied as an example of inheritance."""
	def __init__(self, last_name, eye_color, number_of_toys):
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

billy = Parent("Ray", "Green")
cathy = Child("Ray", "Hazel", 5)
cathy.show_info()
