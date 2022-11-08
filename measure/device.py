from Vector import Vector
from Spline import Spline
from random import random


def rand(a = -1, b = 1):
    return (b - a) * random() + a

def make_target(i):
    return Vector(
        random() * i + 1,
        random() * i + 1
    )

def make_Spline(target):
    begin = Vector(0, 0)
    end = Vector(target)
    diff = end - begin

    #the start of the spline has to go out with angle 0
    control_begin = begin + 3 * abs(diff)**.5 * Vector(1, 0)

    #the Spline should enter the target at an angle
    rotation = [[0, 1], [-1, 0], [0, 0, 1]] #±90°
    off_axis = diff.mmul(rotation)
    control_end = end + 3 * rand() * off_axis
    return Spline (
        begin, end, 
        control_begin, 
        control_end
    )

def measure():
    for i in range(1, 20):
        target = make_target(i).round() #to integer precision
        spline = make_Spline(target)
        
        dt = 1.0 / (20 * i)
        prevv = spline(0)
        prevα = 0
        for T in range(1, 20 * i + 1):
            t = dt * T
            v = spline(t)
            dv = v - prevv
            ds = abs(dv) #step
            α = dv.angle()
            dα = α - prevα
            
            yield {
                "moving": True,
                "angle_change": dα,
                "step": ds
            }
            prevv = v
            prevα = α
        
        yield {
            "moving": False,
            "final_x": target.x,
            "final_y": target.y,
            "final_angle": α
        }

