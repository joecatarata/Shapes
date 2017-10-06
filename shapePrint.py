import sys

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

def drawRightTriangle(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawDiamond(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	spaces = int(height/2)
	for i in range(0, int(height/2)):
		
		for j in range(0, int(spaces)):
			sys.stdout.write(" ")

		for j in range(0, int(spaces-i)):
			sys.stdout.write("*")
		print("\n")



	spaces = 0

	############################################################################
	# END CODE HERE					                                           #
	############################################################################

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
