#Author @tiggreen

from turtle import *

def cross(s, n):
	if n == 1:
		forward(s)
		pu()
		back(s)
	if n > 1: 
		forward(s)
		left(90)
		cross(s/2, n -1)
		right(90)
		pd()
		cross(s/2, n -1)
		right(90)
		pd()
		cross(s/2, n - 1)
		left(90)
		back(s)

def main():
	cross(100, 4)
	input("Press Enter to close the window.")

main()
		
		