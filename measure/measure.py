from device import measure
from Turtle import setup, home, goto, draw_dot, turtle
from math import cos, sin

def main(draw = True):
    setup()
    angle = 0
    pos = [0, 0]
    for measurement in measure():
        if measurement["moving"]:
            angle += measurement["angle_change"]
            step = measurement["step"]
            pos[0] = pos[0] + cos(angle) * step
            pos[1] = pos[1] + sin(angle) * step
            if draw:
                goto(pos)
                turtle.update()
        else:
            final_pos = [
                measurement["final_x"],
                measurement["final_y"]
            ]
            final_angle = measurement["final_angle"]
            print(f"pos: own {pos}, sent {final_pos}, ", 
                end="\t")
            print(f"ang: own {angle}, sent {final_angle}")
            pos = [0, 0]
            angle = 0
            if draw:
                draw_dot(final_pos)
                home()
                turtle.update()
                #input("press [ENTER] to continue")
                #turtle.clear()

if __name__ == "__main__":
    main()
