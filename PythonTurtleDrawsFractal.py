# A turtle draws a fractal that is a circle with squares
# derived from Programming Foundations with Python on Udacity.com

import turtle
import webbrowser

def draw_square(some_turtle):
	for i in range(0, 4):
		some_turtle.forward(100)
		some_turtle.right(90)


def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(3)

	webbrowser.open("https://www.youtube.com/watch?v=xoHECVnQC7A&list=PLOwGIqWnQ8XLazEMg6_hZmpl87lXnukXm&index=4")

	for i in range(0, 36):
		draw_square(brad)
		brad.right(10)

	#angie = turtle.Turtle()
	#angie.shape("arrow")
	#angie.color("blue")
	#angie.circle(100)

	window.exitonclick()



draw_art()





