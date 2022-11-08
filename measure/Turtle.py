import turtle

def setup():
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.speed(0)

def goto(pos):
    turtle.goto(pos[0]*10, pos[1]*10)

def draw_dot(pos):
    turtle.pu()
    goto(pos)
    turtle.dot(3)
    turtle.pd()

def home():
    turtle.pu()
    turtle.home()
    turtle.pd()
