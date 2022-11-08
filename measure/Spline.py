from Vector import Vector
import Turtle

class Spline:
    def __init__(self, begin, end, control_begin = None, control_end = None):
        """ creates a new Spline 
            starting (t=0) at begin and 
            ending (t=1) at end
        get a specific point by calling Spline(t)
        """
        self.A = Vector(begin)
        self.B = Vector(end)
        if control_begin is None:
            self.CA = Spline.make_control(self.A, self.B)
        else:
            self.CA = Vector(control_begin)

        if control_end is None:
            self.CB = Spline.make_control(self.B, self.A)
        else:
            self.CB = Vector(control_end)

        self.a = self.CA - self.A #direction vectors at begin
        self.b = self.CB - self.B #and end
        #helper varibles
        self.T = 3*self.B - 3*self.A - 2 * self.a - self.b
        self.U = 2*self.A - 2*self.B + self.a + self.b

    def __call__(self, t):
        return (
            self.A +
            self.a * t +
            self.T * (t ** 2) +
            self.U * (t ** 3)
        )


    def draw(self, goto = Turtle.goto, T = [t / 20 for t in range(21)]):
        for t in T:
            goto(self(t))
