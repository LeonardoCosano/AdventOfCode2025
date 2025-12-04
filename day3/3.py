def getPosition(digit, powerbank):
	position = powerbank.find(digit)
	return position

def getHighestDigitInRange(strNumber, lowIndex, highIndex):
	listOfDigits = []

	for digit in strNumber[lowIndex:highIndex]:
		listOfDigits.append(digit)

	listOfDigits.sort(reverse=True)
	return listOfDigits[0]

def computeJoltage(firstDigit, secondDigit):
	strNumber = firstDigit + secondDigit
	return int(strNumber)

def sumJoltages(joltage, totalJoltage):
	futureJoltage = totalJoltage + int(joltage)
	return futureJoltage

def main():
	totalJoltage = 0

	# Read battery bank 
	file = open("3.txt")
	for powerbank in file:
		highestDigit = getHighestDigitInRange(powerbank, 0, len(powerbank)-2)
		highestDigitPosition = getPosition(highestDigit, powerbank)
		SecondHighestDigit = getHighestDigitInRange(powerbank, highestDigitPosition+1, len(powerbank)-1)
		joltage = computeJoltage(highestDigit, SecondHighestDigit)
		totalJoltage = sumJoltages(totalJoltage, joltage)

	print ("Amount of joltage is " + str(totalJoltage))

if __name__ == '__main__':
	main()