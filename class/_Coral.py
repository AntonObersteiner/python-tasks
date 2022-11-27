
from random import random
import turtle

## basics of the simulation
#used in the algorithm to determine what particle sticks
threshold = 2
particle_number = 1000

## details of the simulation
fall_speed = 3
#how many falling particles to randomly move somewhere else
reposition_probability = 5 #of the particles
#how many inital non-moving particles to place
seeds = 5

## visualization
#frame of coordinates in which to draw
height = 100
width = 200
#how much to stretch the coordinates to get pixel positions to draw
draw_scale_x = 5
draw_scale_y = 4
#how large to draw the particles
dot_size = 10
#whether the turtle redraws so falling can be shown or whether it 
#just shows the newly appearing particles
redraw_mode = True
#how many generations until once around the color wheel
color_wrap_at = 20


def wrap(x, y):
    while y < 0:        y += height
    while y >= height:  y -= height
    while x < 0:        x += width
    while x >= width:   x -= width
    return x, y

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def rand(lower = -.5, upper = .5):
    return random() * (upper - lower) + lower

def hsv(hue, sat = 1.0, brightness = 1.0):
    "returns some rgb values that behave roughly as expected"
    r, g, b = 0, 0, 0
    h1, h2, h3 = 1.0/3, 2.0/3, 1.0
    if   hue < h1: r = (h1 - hue) * 3
    elif hue > h2: r = (hue - h2) * 3
    if   hue < h1: g = (hue) * 3
    elif hue < h2: g = (h2 - hue) * 3
    if   hue > h2: b = (h3 - hue) * 3
    elif hue > h1: b = (hue - h1) * 3
    
    avg = (r + g + b) / 3
    r = r + (1 - sat) * (avg - r)
    g = g + (1 - sat) * (avg - g)
    b = b + (1 - sat) * (avg - b)

    r *= brightness
    g *= brightness
    b *= brightness

    return r, g, b

def hsv_test():
    turtle.tracer(0, 0)
    turtle.pu()
    for x in range(0, 500, 20):
        for y in range(0, 600, 20):
            hue = x / 500
            sat = y / 600
            brightness = y / 600
            turtle.goto(x, y - 300)
            turtle.color(hsv(hue, sat, 1.0))
            turtle.dot(30)
            turtle.goto(-x, y - 300)
            turtle.color(hsv(hue, 1.0, brightness))
            turtle.dot(30)
    turtle.update()

class Particle:
    def __init__(self, 
        x = None, 
        y = None, 
        fix = False,
        parent = None
    ):
        self.x = rand() * width  if x is None else x
        self.y = rand() * height if y is None else y
        self.fix = fix
        self.parent = parent
        self.color = (.1, .7, .3) #green-ish
        self.level = 0 #when fixed, inherit the parent's plus one

    def __repr__(self):
        return f"({round(self.x)}, {round(self.y)}{', fix' if self.fix else ''})"

    def move(self):
        self.x += random() - 0.5
        self.y -= random() * fall_speed
        self.x, self.y = wrap(self.x, self.y)

    def indices(self):
        x, y = wrap(self.x, self.y)
        i = int(x)
        j = int(y)
        return i, j

    def update_color(self):
        self.color = hsv((self.level % color_wrap_at) / color_wrap_at)
            
    def check(self, background):
        i, j = self.indices()
        own_cell = background[i][j]
        for di in range(- 2, 3):
            for dj in range(- 2, 3):
                I, J = wrap(i + di, j + dj)
                cell = background[I][J]
                for fixed in cell:
                    d = dist(fixed.x, fixed.y, self.x, self.y)
                    if d < threshold:
                        self.parent = fixed #might not be the minimial neighbor
                        self.level = self.parent.level + 1
                        self.update_color()
                        own_cell.append(self)
                        self.fix = True
                        return True
        return False

    def entry(self, background):
        if not self.fix:
            return
        i, j = self.indices()
        cell = background[i][j]
        if self not in cell:
            cell.append(self)

    def draw(self):
        turtle.color(self.color)
        goto(self.x, self.y)
        turtle.dot(dot_size)

def goto(x, y):
    turtle.goto(
        (x - width / 2) * draw_scale_x, 
        (y - height / 2) * draw_scale_y
    )

def make_background(fixed_particles):
    result = [
        [[] for _ in range(height)]
        for _ in range(width)
    ]
    for fix in fixed_particles:
        fix.entry(result)
    return result

def setup():
    turtle.hideturtle()
    turtle.penup()
    if redraw_mode:
        turtle.tracer(0, 0)

def draw(particles):
    for particle in particles:
        particle.draw()

def main():
    setup()
    free = [Particle() for _ in range(particle_number)]
    fix = [
        Particle((s + .5) / seeds * width, 10, True)
        for s in range(seeds)
    ]
    draw(fix)
    background = make_background(fix)
    while True:
        for p in range(len(free)-1, -1, -1):
            if random() <= reposition_probability / particle_number:
                free[p] = Particle() #replace by random particle
            particle = free[p] #alias
            particle.move()
            particle.check(background)
            if particle.fix:
                free.pop(p)
                fix.append(particle)
                particle.draw()
        if redraw_mode:
            turtle.clear()
            turtle.color(.2, .8, .2)
            draw(free)
            turtle.color(0, .2, 1)
            draw(fix)
            turtle.update()

        if len(free) == 0:
            break
    input("[ENTER] to quit.")

if __name__ == "__main__":
    main()
