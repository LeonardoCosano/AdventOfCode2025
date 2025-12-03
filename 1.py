def identifyRotation(line):
	amount = int(line[1:])
	rotation = line[0]
	if rotation == "L":
		rotation = 0
	else:
		rotation = 1

	return rotation, amount

def updateArrow(currentArrowPosition, rotation, amount):
	futureArrowPosition = 0
	if rotation == 0:
		futureArrowPosition = currentArrowPosition - amount
	else:
		futureArrowPosition = currentArrowPosition + amount

	if futureArrowPosition >= 0 and futureArrowPosition <= 99:
		return futureArrowPosition

	if futureArrowPosition < 0:
		overflow = 0 - futureArrowPosition
		futureArrowPosition = 100 - overflow
		return futureArrowPosition

	overflow = futureArrowPosition - 99
	futureArrowPosition = -1 + overflow
	return futureArrowPosition

def updatePassword(arrowPosition, currentPassword):
	newPassword = currentPassword
	if arrowPosition == 0:
		newPassword = newPassword + 1

	return newPassword


def main():

	# Define the safe
	dial = list(range(0,100))
	arrowPosition = 50

	# Define the password
	password = 0

	# Read instructions
	instructions = open("1input.txt")
	for line in instructions:
	  rotation, amount = identifyRotation(line)
	  arrowPosition = updateArrow(arrowPosition, rotation, amount)
	  password = updatePassword(arrowPosition, password)
	  if amount == 79 or amount == 148:
	  	print ("Rotating " + str(amount) + " positions to the " + line[0] + " so new position is " + str(arrowPosition))
	  
	print ("Number of times the safe's dial pointed 0 is " + str(password))


if __name__ == '__main__':
	main()