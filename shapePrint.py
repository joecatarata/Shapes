<<<<<<< HEAD
 def drawSquare(side):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawRectangle(length,width):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################	
=======
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
>>>>>>> develop

def drawRightTriangle(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
<<<<<<< HEAD
	pass
=======
        shape = '*'

        for i in range(height):
            print(shape * (i+1))
        
>>>>>>> develop
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawDiamond(height):
<<<<<<< HEAD
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
=======
<<<<<<< HEAD
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	spaces = int(height/2)
	for i in range(0, int(height/2)):

	for i in range(0, height/2):
		
		for j in range(0, int(spaces)):
			sys.stdout.write(" ")

		for j in range(0, int(spaces-i)):
			sys.stdout.write("*")
		print("\n")



	spaces = 0

>>>>>>> develop
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

<<<<<<< HEAD
=======

>>>>>>> develop
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
