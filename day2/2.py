def getAllIdsIn(collapsedIdRange):
	dashIndex = collapsedIdRange.find("-")
	firstValue = int(collapsedIdRange[0:dashIndex])
	lastValue = int(collapsedIdRange[dashIndex+1:])

	ids = list(range(firstValue,lastValue+1))
	return ids

def getInvalidIds(idRange):
	invalidIds = []

	for number in idRange:
		checkNumber(number, invalidIds)

	return invalidIds

def checkNumber(number, invalidIds):
	stringNumber = str(number)
	digits = len(stringNumber)

	#A number composed by an odd amount of digits can't have a sequence of digits repeated twice inside of it so it is valid 
	if digits % 2:
		return 0

	halfOfnumber = int(digits/2)
	firstHalf = stringNumber[:halfOfnumber]
	SecondHalf = stringNumber[halfOfnumber:]
	if firstHalf == SecondHalf:
		invalidIds.append(str(number))
		return 0


def addUpIds(numberList):
	total = 0
	for number in numberList:
		total = total + int(number)

	return total

def main():
	count=0

	# Read IDs
	file = open("2.txt")
	idsRanges = file.read().split(",")
	for collapsedIdRange in idsRanges:
		#Firstly expand the range from 1-4 to ["1","2","3","4"]
		expandedIdRange = getAllIdsIn(collapsedIdRange)
		#Secondly inspect every number ["1","2","3","4"] 
		invalidIds = getInvalidIds(expandedIdRange)
		#Lastly add up its value
		invalidIdsSum = addUpIds(invalidIds)
		count = count + invalidIdsSum

	print ("Sum of invalid ids is: " + str(count))

if __name__ == '__main__':
	main()