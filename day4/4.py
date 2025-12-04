def findRollPaperPositions(row):
	rollPaperPositions = []
	listRow = list(row)	
	while "@" in listRow:
		firstRollPaperPosition = listRow.index("@")
		rollPaperPositions.append(firstRollPaperPosition)
		listRow[firstRollPaperPosition]=(".")

	return rollPaperPositions

def countValidRollPapersInRow(rollPaperPositions, rowIndex, grid, width, height):
	totalValidRollPapers = 0

	for position in rollPaperPositions:
		validRollPaper = checkRollPaper(position, rowIndex, grid, width, height)
		totalValidRollPapers = totalValidRollPapers + validRollPaper

	return totalValidRollPapers

def checkRollPaper(position, rowIndex, grid, width, height):

	countRollPapersAround = 0

	if rowIndex != 0:
		totalRollPapers = countRollPapersAroundInRow(rowIndex-1, position, grid, width)
		countRollPapersAround = totalRollPapers

	totalRollPapers = countRollPapersBeside(rowIndex, position, grid, width)
	countRollPapersAround = countRollPapersAround + totalRollPapers

	if rowIndex != (height-1):
		totalRollPapers = countRollPapersAroundInRow(rowIndex+1, position, grid, width)
		countRollPapersAround = countRollPapersAround + totalRollPapers

	if countRollPapersAround < 4:
		return 1

	return 0

def countRollPapersAroundInRow(rowIndex, position, grid, width):
	countRollPapers = 0
	rollPapersAround = ""
	row = grid[rowIndex]

	if position != 0 and position != (width-1):
		rollPapersAround = row[position-1:position+2]

	# RollPaper is in the Left side of the grid
	if position == 0:
		rollPapersAround = row[0:position+2]

	# RollPaper is in the Right side of the grid
	if position == (width-1):
		rollPapersAround = row[position-2:width]

	countRollPapers = rollPapersAround.count("@")
	return countRollPapers

def countRollPapersBeside(rowIndex, position, grid, width):
	countRollPapers = 0
	rollPapersAround = ""
	row = grid[rowIndex]

	if position != 0 and position != (width-2):
		rollPapersAround = row[position-1] + row[position+1]

	# RollPaper is in the Left side of the grid
	if position == 0:
		rollPapersAround = row[position+1]

	# RollPaper is in the Right side of the grid
	if position == (width-2):
		rollPapersAround = row[position-1]

	countRollPapers = rollPapersAround.count("@")
	return countRollPapers


def main():
	totalAccesibleRollPapers = 0

	#Load the grid in memory
	grid = []
	gridFile = open("4grid.txt")
	for row in gridFile:
		grid.append(row)

	#Define grid properties
	width = len(grid[0])
	height = len(grid)

	#Iterate over grid
	rowIndex = 0
	for row in grid:
		rollPaperPositions = findRollPaperPositions(row)
		accesibleRollPapersInThisRow = countValidRollPapersInRow(rollPaperPositions, rowIndex, grid, width, height)
		totalAccesibleRollPapers = totalAccesibleRollPapers + accesibleRollPapersInThisRow
		rowIndex = rowIndex + 1

	print ("Total number of accesible roll of papers is: " + str(totalAccesibleRollPapers))

if __name__ == '__main__':
	main()