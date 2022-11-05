"""
Hier soll eine Klasse entstehen, die einen 2d-Vektor (x, y) repräsentiert
Diese sollte man addieren, subtrahieren und mit einer Zahl multiplizieren können

Übliche Verwendungen:
a = Vector(5, 2)            #__init__
b = Vector(2, 2)
c = Vector(-1, -1) * 0.2    #__mul__
b += a - b                  #__sub__ und __iadd__
"""


class Vector:
    #neuen Vektor mit Vector(x, y) erzeugen
    #(x und y sollten Zahlen sein)
    def __init__(self, x, y):
        self.x = x

    def __repr__(self):
        return f"V({self.x}, {self.y})"

    #wird verwendet, wenn irgendwo  self == other  gefragt wird
    def __eq__(self, other):
        return (
            isinstance(other, Vector) and
            self.x == other.x and
            other.x == other.y
        )

    #self + other
    def __add__(self, other):
        #other ist ein Vektor! hat .x und .y
        return Vector(
            #einen neuen Vektor mit den Koordinaten der Summe
            self.x + other.x,
            self.y + other.y,
        )

    #self += other
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    #self - other
    def __sub__(self, other):
        return Vector(0, 0) #unvollständig

    #self -= other
    def __isub__(self, other):
        return self #unvollständig

    #self * factor
    def __mul__(self, factor):
        return Vector(0, 0)

    #self *= factor
    def __imul__(self, factor):
        return self

    #abs(self)  Betrag des Vektors
    def __abs__(self):
        #nicht die richtige Funktion...
        return self.x + self.y


"""
Ab hier teste ich die Klasse darauf, ob sie kann, was sie soll
"""
questions = 0
def check(what_is, what_should_be, message):
    global questions
    if what_is != what_should_be:
        print(message, f"{what_is} != {what_should_be}")
        questions += 1

a = Vector(5, 2)            #__init__(5, 2)
try:
    check(a.x, 5, "self.x wurde für a nicht auf 5 gesetzt?")
    check(a.y, 2, "self.y wurde für a nicht auf 2 gesetzt?")
except AttributeError as ae:
    print("Deine Klasse hat in __init__ irgendein self.... nicht angelegt:\n", ae, "\n\n")

b = Vector(2, 2)
c = Vector(-1, -1) * 0.2    #__mul__
check(c, Vector(-.2, -.2), "Vector(-1, -1) * .2 ergibt nicht Vector(-.2, -.2)?")

b -= a                      #__isub__
check(b, Vector(-3, 0), "b - a ergibt nicht das neue b == Vector(3, 0)?")

d = Vector(3, 4)
check(abs(d), 5, "Vector(3, 4) ist nicht 5 lang?")

if questions == 0:
    print("well done, have a cookie")
else:
    print("Either your class isn't done yet or my tests are wrong...")
