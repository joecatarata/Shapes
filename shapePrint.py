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
        shape = '*'

        for i in range(height):
            print(shape * (i+1))
        
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawDiamond(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################


def drawXSquare(length):

	shape = "*"
	spaces = 0
	for i in range(int(length/2)):
		if i == 0 or i == int(length/2 - 1):
			print(shape*length)
		else 
			print()
		


print("----------------------------Shape Printer----------------------------")
while True:
	resp = 0
	while True:
		print("Which shape do you want to draw?")
		print("[1] - Square")
		print("[2] - Rectangle")
		print("[3] - Right Triangle")
		print("[4] - Diamond")
		print("[5] - X-Square")
		print("[9] - Exit")
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
		length = int(input("Enter length: "))
		drawXSquare(length)
	elif resp == 9:
		break
