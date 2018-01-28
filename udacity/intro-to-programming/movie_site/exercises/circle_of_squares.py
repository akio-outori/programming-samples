#!/usr/bin/python

# Quick program to use the turtle built-in to draw a circle of squares.

import turtle

# Create a window and set background color
def create_screen(bg_color):
	window = turtle.Screen()
	window.bgcolor("red")
	return window
	
# Configure the shape, color, and speed of the drawing.
def configure_turtle(shape, color, speed):
	instance = turtle.Turtle()
	instance.shape(shape)
	instance.color(color)
	instance.speed(speed)
	return instance

# Draw a square.  Call this as many times as necessary to draw the desires shape.
def draw_square(instance):
	distance = 100
	turn = 90
	for i in range(0,4):
		instance.forward(distance)
		instance.right(turn)

# Draw a circle of squares by calling the sqar_square function until a circular shape is formed.
def circle_of_squares(instance):
	for i in range(0,36):
		draw_square(instance)
		instance.right(10)

window = create_screen("red")
circle_of_squares(configure_turtle("turtle", "yellow", 5))
window.exitonclick()
