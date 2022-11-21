#!/usr/bin/env python3
"""
Hier soll eine Klasse entstehen, die ein "Auto" implementiert
"""

import turtle
from _Vector import Vector
from math import cos, sin, pi

class Car:
    """
    the Car tries to measure its own position when asked to turn and move
    the discrepancy is shown by making visible the own turtle self.T
        and an extra measurement turtle self.show_turtle
    """

    def __init__(self):
        self.T = turtle.clone()
        turtle.hideturtle()
        self.speed = 1
        self.pos = Vector(0, 0)
        self.angle = 0

        self.show_turtle = turtle.Turtle()
        self.show_turtle.color((.05, .5, .1)) #green
        #self.show_turtle.penup()

    #damit print(some_car) gut funktioniert
    def __repr__(self):
        return f"Car@{self.pos}"

    def left(self, da = 5):
        self.angle += da / 360 * 2*pi
        self.T.left(da)

    def right(self, da = 5):
        self.angle -= da / 360 * 2*pi
        self.T.right(5)

    def sync(self):
        self.angle = self.T.heading() / 360 * 2*pi
        self.pos = Vector(*self.T.pos())

    def move(self):
        self.T.forward(self.speed)
        self.pos += Vector(
            cos(self.angle),
            sin(self.angle)
        ) * self.speed
        self.show_turtle.goto(self.pos.x, self.pos.y)
        turtle.ontimer(self.move, 1)

def main():
    C = Car()
    print("Press 'a' to turn left, 'd' to turn right, '0' to reset and 'Q' to quit")

    turtle.onkeypress(C.left, "a")
    turtle.onkeypress(C.right, "d")
    turtle.onkeypress(C.sync, "0")
    turtle.onkeypress(exit, "Q")
    turtle.listen()

    turtle.ontimer(C.move, 1)
    turtle.mainloop()

if __name__ == '__main__':
    main()
