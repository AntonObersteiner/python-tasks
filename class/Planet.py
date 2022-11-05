#!/usr/bin/env python3

"""
Hier soll eine Klasse entstehen, die einen Planeten mit Position, Masse und Geschwindigkeit repräsentiert
Diese kann man mit einer Kraft beschleunigen und sie sich anziehen lassen.
Sie können mit der Turtle gezeichnet werden.

Übliche Verwendungen:
p1 = Planet(5, Vector(5, 2))            #__init__
p2 = Planet(1, Vector(1, 1))
p1.attract(p2)  #gravity
p2.attract(p1)  #both ways
p1.update() #move a tiny step (and draw with the turtle)
p2.update()
"""

from _Vector import Vector
#wenn ihr keinen fertigen Vector habt, könnt ihr
#from _Vector import Vector
#verwenden

#for drawing, see /tasks/the_turtle.py
import turtle
#wenn ihr eine schnelle Turtle haben wollt, führt das aus:
# turtle.speed(0)
# turtle.delay(0)
# turtle.ht(0)
# turtle.tracer(0, 0)
#jedes mal, wenn ihr sehen wollt, was die Turtle gemalt hat, müsst ihr
# turtle.update()
#aufrufen


dt = .1
G = 100 #find a good value
class Planet(Vector):
    """
    neuen Planeten mit mass und pos = Vector(x, y) erzeugen
    self.vel ist standardmäßig (0, 0)
    ich gebe euch frei, ob ihr die Position als
        class Planet(Vector):
        erben wollt,
        oder ob ihr das als
            self.pos = Vector(x, y)
        implementieren wollt.
        Für Vererbung, schaut in
            /latex/slides/build/02_....pdf, Abschnitt Super- und Sub-Klassen
            und stellt Fragen.
    """
    def __init__(self, mass, pos):
        super(Planet, self).__init__(pos.x, pos.y)
        pass

    def __repr__(self):
        return f"P(m = {self.mass}, vel = {self.vel})"

    def attract(self, other):
        #gravity! see /latex/slides/build/02_...pdf
        pass

    def accel(self, force): #force should be Vector
        pass

    def update(self):
        pass

    def update_and_draw(self):
        #mit turtle machen, damit man endlich die planeten sieht
        #eine Lösung findet sich in
        #/latex/slides/resources/planets/Planet.py
        pass

"""
Ab hier teste ich die Klasse darauf, ob sie kann, was sie soll
"""
questions = 0
def check(what_is, what_should_be, message):
    global questions
    if what_is != what_should_be:
        print(message, f"{what_is} != {what_should_be}")
        questions += 1

def test_get_pos(planet):
    try:
        return planet.pos
    except AttributeError as ae:
        try:
            pos = super(Planet, planet)
            return pos.__add__(Vector(0, 0))
        except Exception as e:
            print("Ich konnte weder ein Attribut .pos bei deinem Planeten noch eine Vererbung von Vector finden :(")
            print(f"AttributeError: {ae}")
            print(f"Exception: {e}")

def test():
    global questions
    a = Planet(5, Vector(6, 7))            #__init__

    try:
        check(a.mass, 5, "self.mass wurde für a nicht auf 5 gesetzt?")
        check(a.vel.x, 0, "self.vel wurde für a nicht auf (0, 0) gesetzt?")
        pos = test_get_pos(a)
        check(pos, Vector(6, 7), "die Position deines Planete wurde für a nicht auf (6, 7) gesetzt?")
    except AttributeError as ae:
        print("Deine Klasse hat in __init__ irgendein self.... nicht angelegt:\n", ae, "\n\n")
        questions += 1

    def test_update():
        global dt
        dt = .1

        a.vel = Vector(1, -1)
        a.update()
        pos = test_get_pos(a)
        check(pos, Vector(6.1, 6.9), "nach update mit Position (6, 7)  +   vel = (1, -1)  *  dt = .1: neue Position scheint falsch: ")

    def test_accel():
        global dt
        dt = .1

        a.vel = Vector(1, -1)
        a.mass = 5
        force = Vector(5, 5)
        a.accel(force)
        #acc = force / a.mass = (1, 1)
        #change to vel: acc * dt
        check(a.vel, Vector(1.1, -0.9), "nach accel mit vel = (1, -1) +  force = (5, 5) / mass = 5 * dt = .1: neue Geschwindigkeit scheint falsch: ")

    def test_attract():
        global dt
        dt = .1

        a = Planet(1, Vector(2, 0))
        b = Planet(2, Vector(0, 2))

        diff = b - a
        dist = abs(diff)
        #keine Zeit, evtl selbst Beispiel durchrechnen und damit die funktion überprüfen
        should_be = Vector(0, 0)

        a.attract(b)

        # check(a.vel, should_be, "attract scheint nicht richtig zu funktionieren!")

    test_update()
    test_accel()
    test_attract()


if __name__ == '__main__':
    test()

    if questions == 0:
        print("well done, have a cookie")
    else:
        print("Either your class isn't done yet or my tests are wrong...")
