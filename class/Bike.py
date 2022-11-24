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

        #zum Zeigen der gemessenen Position
        self.show_turtle = turtle.Turtle()
        self.show_turtle.hideturtle()

    #damit print(vehicle) und str(vehicle) funktioniert
    def __repr__(self):
        return f"Vehicle@{self.pos}"

    def left(self, da = 5):

    def right(self, da = 5):

    def sync(self):
        #tatsächliche Position aus der Turtle kopieren
        self.pos = list(self.T.position())
        self.angle = self.T.heading() / 360 * 2 * pi

    def move(self):
        #fährt immer wieder in die aktuelle Richtung
        #die "gemessene" Position wird gemalt

        #diese-Funktion ruft sich immer wieder selbst auf,
        #damit es weiterfährt
        turtle.ontimer(self.move, 1)

def main():
    #ein Objekt wird erzeugt
    myBike = Vehicle()

    #Tasten werden an die Methoden der Funktion gebunden
    turtle.onkeypress(myBike.left, "a")
    turtle.onkeypress(myBike.right, "d")
    turtle.onkeypress(myBike.sync, "0")
    turtle.onkeypress(exit, "Q")
    turtle.listen() #damit die Tasten auch gehört werden

    turtle.ontimer(myVehicle.move, 1) #anfangen, das aufzurufen
    turtle.mainloop()

if __name__ == '__main__':
    main()
