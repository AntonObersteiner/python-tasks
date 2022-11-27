
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
#how many generations until once around the color wheel
color_wrap_at = 20


def wrap(x, y):
    "wraps around x and y so that 0 <= x < width and 0 <= y < height"
    return x % width, y % height

def dist(x1, y1, x2, y2):
    "returns the euclidian distance √(Δx² + Δy²) from (x₁, y₁) to (x₂, y₂)"
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def hsv(hue, sat = 1.0, brightness = 1.0):
    """returns rgb values so that
        hue wraps goes around the colorwheel,
        sat describes the saturation (aka non-averaging) and 
        brightness is roughly the magnitude.
    actually, this implements just triangle interpolation"""

    r, g, b = 0, 0, 0
    h = hue * 3
    if   h < 1.0: r = 1.0 - h
    elif h > 2.0: r = h - 2.0
    if   h < 1.0: g = h
    elif h < 2.0: g = 2.0 - h
    if   h > 2.0: b = 3.0 - h
    elif h > 1.0: b = h - 1.0
    
    #interpolate each value with the average
    avg = (r + g + b) / 3
    r = r + (1 - sat) * (avg - r)
    g = g + (1 - sat) * (avg - g)
    b = b + (1 - sat) * (avg - b)

    #scale each value with the brightness
    r *= brightness
    g *= brightness
    b *= brightness

    return r, g, b

class Particle:
    def __init__(self, fix = False):
        self.x = random() * width
        self.y = random() * height
        self.fix = fix
        self.parent = None
        self.color = (.8, .8, .90) #bluish-ish white
        self.dot_size = 1
        self.level = 0 #when fixed, inherit the parent's plus one
        if self.fix:
            #seeds should get their color set according to their level
            self.update_color_and_size()

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

    def update_color_and_size(self):
        self.color = hsv((self.level % color_wrap_at) / color_wrap_at)
        self.dot_size = 10

    def bind(self, parent):
        "binds to a parent, inherits their level (+ 1), updates color and size"
        self.parent = parent
        self.level = self.parent.level + 1
        self.update_color_and_size()

            
    def check(self, background):
        own_i, own_j = self.indices()
        own_cell = background[own_i][own_j]

        for i in range(own_i - 2, own_i + 3):
            for j in range(own_j - 2, own_j + 3):
                i, j = wrap(i, j)
                for fixed in background[i][j]:
                    d = dist(fixed.x, fixed.y, self.x, self.y)
                    if d < threshold:
                        #note that we bind to the first close fixed particle,
                        #not nessecarily the closest fixed particle
                        self.bind(fixed)
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
        turtle.dot(self.dot_size)


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
    turtle.tracer(0, 0)

def main():
    setup()
    free = [Particle() for _ in range(particle_number)]
    fix = []
    for s in range(seeds):
        fixed = Particle(fix = True)
        fixed.x = (s + .5) / seeds * width
        fixed.y = 10
        fixed.draw()
        fix.append(fixed)

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
            else:
                particle.draw()
        turtle.update()

        if len(free) == 0:
            break
    input("[ENTER] to quit.")

if __name__ == "__main__":
    main()
