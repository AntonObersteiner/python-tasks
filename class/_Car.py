#!/usr/bin/env python3
"""
Hier soll eine Klasse entstehen, die ein "Auto" implementiert
"""

import turtle
from _Vector import Vector
from math import cos, sin, pi

class Car:
    def __init__(self):
        self.T = turtle.clone()
        self.speed = 1
        self.pos = Vector()
        self.angle = 0
        self.show_turtle = turtle.Turtle()
        self.show_turtle.pu()

    #damit print(mensch) gut funktioniert
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
        self.T.fd(self.speed)
        self.pos += Vector(
            cos(self.angle), sin(self.angle)
        ) * self.speed
        self.show_turtle.goto(self.pos.x, self.pos.y)
        turtle.ontimer(self.move, 1)

def main():
    C = Car()

    turtle.onkeypress(C.left, "a")
    turtle.onkeypress(C.right, "d")
    turtle.onkeypress(C.sync, "0")
    turtle.onkeypress(exit, "Q")
    turtle.listen()

    turtle.ontimer(C.move, 1)
    turtle.mainloop()

if __name__ == '__main__':
    main()
