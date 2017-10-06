import sys

def drawSquare(side):
	for i in range(0, side):
		for x in range(0, side):
			sys.stdout.write('* ')
		print ('')

def drawRectangle(length,width):

	for i in range(0,length):
		for y in range(0,width):
			sys.stdout.write("*")
		print("")

def drawRightTriangle(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
        shape = '*'

        for i in range(height):
            print(shape * (i+1))
        
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawDiamond(height):
	spaces = height/2

	for i in range(0, height/2):
		
		for j in range(0, height):

print("----------------------------Shape Printer----------------------------")
while True:
	resp = 0
	while True:
		print("Which shape do you want to draw?")
		print("[1] - Square")
		print("[2] - Rectangle")
		print("[3] - Right Triangle")
		print("[4] - Diamond")
		print("[5] - Exit")
		try:
			resp = int(input("Response: "))
			if resp >= 1 and resp <= 5:
				break
			else:
				print("Response must be from 1 to 5")
		except ValueError:
			print("Input must be a number")

	if resp == 1:
		side = int(input("Enter side length: "))
		drawSquare(side)
	elif resp == 2:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		drawRectangle(length,width)
	elif resp == 3:
		height = int(input("Enter height: "))
		drawRightTriangle(height)
	elif resp == 4:
		height = int(input("Enter height: "))
		drawDiamond(height)
	elif resp == 5:
		break
