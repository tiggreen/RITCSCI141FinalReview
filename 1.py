#Author @tiggreen

from turtle import *

def draw(s, n, degree):
	for i in range(n):
		forward(s)
		right(degree)

def crc(rad):
	circle(rad)


# iterative way
def drawCircle(radius):
	#length of the circumference
	c = 2 * pi * radius
	for angle in range(360):
		forward(c/360)
		left(1)


	
def main():
	#draw(150, 6, 60)
	#crc(60)
	drawCircle(60)
	input("Enter to exit the program.")

main()

	