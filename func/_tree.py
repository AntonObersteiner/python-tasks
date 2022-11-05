import turtle

turtle.speed(0)
turtle.delay(0)
turtle.tracer(0, 0)

angle = 20
length = 50
inner = .9 * length
shrink = .8
leaf_width = 5

def segment(depth = 0, max_depth = 5):
    if depth == max_depth:
        turtle.fillcolor(0, depth / max_depth, 0)
        turtle.begin_fill()

        turtle.right(30)
        turtle.forward(20)
        turtle.left(120)
        turtle.forward(20 + leaf_width)
        turtle.left(120)
        turtle.forward(20)
        turtle.left(150)

        turtle.end_fill()
        return

    print(f"{' '*depth}Tiefe: {depth}")
    factor = shrink ** depth

    turtle.right(angle)
    turtle.forward(length * factor)

    segment(depth + 1, max_depth)

    turtle.backward(inner * factor)
    turtle.left(2 * angle)
    turtle.forward(inner * factor)

    segment(depth + 1, max_depth)

    turtle.backward(length * factor)
    turtle.right(angle)

#these functions can later be bound to specific keys and so the image changes with '+' or other keys
def increment_angle(): global angle; angle += 1; redraw()
def decrement_angle(): global angle; angle -= 1; redraw()

def increment_length(): global length; length *= 1.01; redraw()
def decrement_length(): global length; length /= 1.01; redraw()

def increment_leaf_width(): global leaf_width; leaf_width += 1; redraw()
def decrement_leaf_width(): global leaf_width; leaf_width -= 1; redraw()

def redraw():
    turtle.home()
    turtle.clear()
    segment(0, 5)
    turtle.update()

if __name__ == '__main__':
    #here, I tell the turtle which function to call when I press a certain key
    turtle.onkeypress(increment_angle, 'plus')
    turtle.onkeypress(decrement_angle, 'minus')
    turtle.onkeypress(increment_length, 'asterisk')
    turtle.onkeypress(decrement_length, 'slash')
    turtle.onkeypress(increment_leaf_width, 'Up')
    turtle.onkeypress(decrement_leaf_width, 'Down')
    turtle.listen()

    redraw()
    input("[ENTER] to quit")
