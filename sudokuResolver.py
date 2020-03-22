# TL : 22-03-20 : Here is my sudoku solver.
# You just need to change de digits in the global variable and run the script to complete your sudoku. Each list represents a line.
# If your grid comes back unchanged, then the sudoku wasn't valid.



grille = [
    [4,0,8,0,0,7,0,0,0],
    [0,3,0,9,0,0,0,0,0],
    [9,0,0,8,0,4,7,3,0],
    [6,0,7,0,0,3,0,5,0],
    [1,0,0,0,0,0,0,0,3],
    [0,5,0,6,0,0,4,0,7],
    [0,2,4,5,0,1,0,0,6],
    [0,0,0,0,0,6,0,8,0],
    [0,0,0,7,0,0,2,0,1]
]

def alreadyExistsInRow(grid, number, position):
    """" Function that determines if a number already exist in the row containing the current box, for the entire grid. """
    row = (position // 9) # Every 9 boxes we go to the next line.
    row = (row - 1) if (position % 9 == 0) else row # Because if position % 9 = 0, the row is too great by 1.
    return number in grid[row]

def alreadyExistsInColumn(grid, number, position):
    """" Function that determines if a number already exist in the column containing the current box, for the entire grid. """
    column = (position % 9) - 1 # Couting the 0.
    for row in grid:
        if(row[column] == number):
            return True
    return False

def alreadyExistsInArea(grid, number, position):
    """ Function that determines if a number already exist in the sub-grid containing the current box. """
    row = (position // 9)
    row = (row - 1) if (position % 9 == 0) else row # Because if position % 9 = 0, the row is too great by 1.
    column = (position % 9) - 1 # Counting the 0.
    initialRow = (row // 3) * 3 # Determines the first row to check.
    initialColumn = (column // 3) * 3 # Determines the first column to check.
    for i in range(initialRow, initialRow + 3): # A sub-grid is a 3X3 square.
        for j in range(initialColumn, initialColumn + 3):
            if (grid[i][j] == number):
                return True
    return False

def canBeWritten(grid, number, position):
    """ Function that determines if a number can be inserted according to the rules of the sudoku. """
    return ((not(alreadyExistsInArea(grid, number, position))) and (not(alreadyExistsInColumn(grid, number, position))) and (not(alreadyExistsInRow(grid, number, position))))

def displayGrid(grid):
    """ Function that draws the grid and the digits inside. """
    rowCounter = 0
    print("------------") # The top of the grid.
    for row in grid:
        boxCounter = 0
        print("|", end="")
        for box in row:
            print(box, end="")
            boxCounter += 1
            if (boxCounter % 3 == 0):
                print("|", end="") # Vertical separation between each sub-grid.
        print("")
        rowCounter += 1
        if(rowCounter % 3 == 0):
            print("------------") # Horizontal separation between each sub-grid.



def completeSudoku(grid, position):
    """ Function that tries to complete the sudoku."""

    # If we are at the end of the grid.
    if (position == 82):
        return True

    row = position // 9
    row = (row - 1) if (position % 9 == 0) else row # Because if position % 9 = 0, the row is too great by 1.
    column =  (position % 9) - 1 # Counting the 0.

    if (grid[row][column] != 0):
        return completeSudoku(grid, position + 1)


    for i in range(1, 10): # Every possible digit that we can write in a box.
        if (canBeWritten(grid, i, position)):
            grid[row][column] = i
            if(completeSudoku(grid, position + 1)):
                return True
        

    grid[row][column] = 0
    return False





print("Initial state grid :")
displayGrid(grille)
completeSudoku(grille,1)
print("Grid after treatment :")
displayGrid(grille)