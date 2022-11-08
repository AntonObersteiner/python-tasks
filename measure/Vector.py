from math import atan2

class Vector:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) not in [float, int]:
            #assume this is something iterable like a tuple, list or vector
            args = args[0]
        self.x = args[0] if len(args) > 0 else 0
        self.y = args[1] if len(args) > 1 else 0
        self.z = args[2] if len(args) > 2 else 0
    def __repr__(s): return f"({round(s.x, 3):5}, {round(s.y, 3):5}, {round(s.z, 3):5})"
    def __len__(self):
        return 3
    def __getitem__(self, key):
        match key:
            case 0: return self.x
            case 1: return self.y
            case 2: return self.z
            case "x": return self.x
            case "y": return self.y
            case "z": return self.z
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    def __add__(s, o): o = Vector(o); return Vector(s.x+o.x, s.y+o.y, s.z+o.z)
    def __sub__(s, o): o = Vector(o); return Vector(s.x-o.x, s.y-o.y, s.z-o.z)
    def __mul__(s, f): return Vector(s.x*f, s.y*f, s.z*f)
    def __radd__(s, o): return s.__add__(o)
    def __rmul__(s, f): return s.__mul__(f)
    def __iadd__(s, o): o = Vector(o); s.x += o.x; s.y += o.y; s.z += o.z
    def __imul__(s, f): s.x *= f; s.y *= f; s.z *= f
    def dotp(s, o): o = Vector(o); return s.x * o.x + s.y * o.y + s.z * o.z
    def mmul(s, m): return s.x*Vector(m[0]) + s.y*Vector(m[1]) + s.z*Vector(m[2])
    def __abs__(s): return (s.x**2 + s.y**2 + s.z**2)**.5
    def dist(s, o): return abs(s-o)
    def angle(s): return atan2(s.y, s.x)
    def map(s, fun): return Vector(fun(s.x), fun(s.y), fun(s.z))
    def round(s, digits = 0): return s.map(lambda x: round(x, digits))
