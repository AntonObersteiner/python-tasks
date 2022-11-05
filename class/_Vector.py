class Vector:
    #neuen Vektor mit Vector(x, y) erzeugen
    #(x und y sollten Zahlen sein)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"V({self.x}, {self.y})"
    def __eq__(self, other):
        return (
            isinstance(other, Vector) and
            self.x == other.x and
            self.y == other.y
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
        return Vector(
            #einen neuen Vektor mit den Koordinaten der Summe
            self.x - other.x,
            self.y - other.y,
        )

    #self -= other
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self #unvollständig

    def __mul__(self, factor):
        return Vector(
            #einen neuen Vektor mit den Koordinaten der Summe
            self.x * factor,
            self.y * factor,
        )

    def __imul__(self, factor):
        self.x *= factor
        self.y *= factor
        return self

    #abs(self)  Betrag des Vektors
    def __abs__(self):
        #nicht die richtige Funktion...
        return (self.x ** 2 + self.y ** 2) ** .5
