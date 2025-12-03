def TwoHighestValues(powerbank):
	listOfDigits = []
	for digit in powerbank:
		listOfDigits.append(digit)
	listOfDigits.sort(reverse=True)
	print(listOfDigits)
	return listOfDigits[0], listOfDigits[1]

def getJoltage(powerbank, highestValues):
	indexFromHighestValue = powerbank.find(highestValues[0])
	indexFrom2HighestValue = powerbank.find(highestValues[1])

	if indexFromHighestValue < indexFrom2HighestValue:
		print (highestValues[0] + highestValues[1])
		return (highestValues[0] + highestValues[1])

	print (highestValues[1] + highestValues[0])
	return (highestValues[1] + highestValues[0])

def sumJoltages(joltage, totalJoltage):
	futureJoltage = totalJoltage + int(joltage)
	return futureJoltage

def main():
	totalJoltage = 0

	# Read battery bank 
	file = open("3.txt")
	for powerbank in file:
		print (powerbank)
		highestValues = TwoHighestValues(powerbank)
		joltage = getJoltage(powerbank, highestValues)
		totalJoltage = sumJoltages(joltage, totalJoltage)

	print ("Amount of joltage is " + str(totalJoltage))

if __name__ == '__main__':
	main()