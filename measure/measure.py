"""
your job: you get measurements from a function called measure
	what measurements? it tells you. print(help(measure))
don't call measure yourself, it's a bit special and should be called in a for loop
	see line 22
use the data in the for-loop-variable measurement to track the position.
	eventually, it tells you it's not moving any more and you can check your estimation
you will be off a bit, because a sensor is broken
	but you can recalibrate and should be spot-on afterwards
"""

from device import measure
from Turtle import setup, home, goto, draw_dot, turtle
from math import cos, sin

def main(draw = True):
	setup() #makes turtle work better

	#initialize your variables


	for measurement in measure():
		if measurement["moving"]:
			#update your knowledge


			if draw:
				goto(position)
				turtle.update()
		else:
			#if measurement["moving"] == False, it tells you the final position,
			#now check against your solution, maybe use to calibrate...

			#best: give some debug info

			#reset your variables (the new 'measurement run' starts
			# at (0, 0), angle 0)


			if draw:
				draw_dot(final_pos)
				home()
				turtle.update()
				#input("press [ENTER] to continue")
				#turtle.clear()

if __name__ == "__main__":
	main()
