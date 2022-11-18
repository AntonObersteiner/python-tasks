import turtle
from math import sin, cos, pi

# die Turtle beginnt immer bei (0, 0), also im Zentrum
# wohin mit dem pendown, damit bei dem Stern keine Linie 
# von (0, 0) nach oben führt?
turtle.penup() #setzt Stift auf/beginnt zu zeichnen
turtle.pendown() #hebt Stift an/zeichnet erstmal nicht weiter


def draw_star(points):
    """soll Stern mit <points> Spitzen zeichnen, malt aber immer einen mit 5"""
	turtle.fillcolor(.5, .1, .9)
	turtle.begin_fill() # beginnt Füll-Modus

	for i in range(0, 6):
	    angle = i * 2 * pi / 5 * 2
	    x = 200 * sin(angle)
	    y = 200 * cos(angle)
	    turtle.goto(x, y)

    # hier wird der Füll-Modus beendet, sodass alles, 
    # was dazwischen gezeichnet wurde, gefüllt wird
	turtle.end_fill()

if __name__ == '__main__':
	draw_star(5)
	input("Waiting for user... press [ENTER] to quit")
