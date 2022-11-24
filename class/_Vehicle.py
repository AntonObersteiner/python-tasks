#!/usr/bin/env python3
"""
Hier soll eine Klasse entstehen, die ein "Fahrzeug" implementiert
Eine Turtle wird mit den Pfeiltasten nach links und rechts gesteuert.
Gleichzeitig rechnet das "Vehicle" mit, wo es ist (dazu die Imports aus math)
Es fehlen noch ein paar Dinge, mit #TODO markiert

Am Besten mal https://docs.python.org/3/library/turtle.html überfliegen
"""

import turtle
from math import cos, sin, pi

class Vehicle:
    def __init__(self):
        #Vehicle kontrolliert eine Turtle
        self.T = turtle.Turtle()

        #Startposition und -zustand
        self.pos = [0, 0]
        self.angle = 0

        #zum Zeigen der gemessenen Position
        self.show_turtle = turtle.Turtle()
        self.show_turtle.hideturtle()

    #damit print(mensch) und str(mensch) funktioniert
    def __repr__(self):
        return f"Vehicle@{self.pos}"

    def left(self, da = 5):
        self.T.left(da)
        self.angle += da / 360 * 2 * pi

    def right(self, da = 5):
        self.left( - da)

    def sync(self):
        #tatsächliche Position aus der Turtle kopieren
        self.pos = list(self.T.position())
        self.angle = self.T.heading() / 360 * 2 * pi

    def move(self):
        #fährt immer wieder in die aktuelle Richtung
        self.T.forward(1)
        self.pos[0] += cos(self.angle)
        self.pos[1] += sin(self.angle)

        #die "gemessene" Position wird gemalt
        self.show_turtle.goto(self.pos)

        #diese-Funktion ruft sich immer wieder selbst auf,
        #damit es weiterfährt
        turtle.ontimer(self.move, 1)

def main():
    #ein Objekt wird erzeugt
    myVehicle = Vehicle()

    #Tasten werden an die Methoden der Funktion gebunden
    turtle.onkeypress(myVehicle.left, "a")
    turtle.onkeypress(myVehicle.right, "d")
    turtle.onkeypress(myVehicle.sync, "0")
    turtle.onkeypress(exit, "Q")
    turtle.listen() #damit die Tasten auch gehört werden

    turtle.ontimer(myVehicle.move, 1) #anfangen, das immer wieder aufzurufen
    turtle.mainloop()

if __name__ == '__main__':
    main()
