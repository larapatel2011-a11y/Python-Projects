import random

grid= [["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"]]
print(grid)
def displaygrid():
    for row in grid:
        for column in row:
            print (column,end = ' ')
        print('')

trow = random.randint (0,4)
tcolumn = random.randint (0,4)

print (trow, tcolumn)

prow = 0
pcolumn = 0

while True:

    displaygrid()
    row = int(input("Guess the row number: (0 - 4): "))
    column = int(input("Guess the column number (0 - 4): "))
    grid [prow][pcolumn] = "_"
    grid [row][column] = "!"
    prow = row
    pcolumn = column

    if row == trow and column == tcolumn:
        print("You found the right spot")
        break

    elif column < tcolumn:
        print("Move right")
    elif column > tcolumn:
        print("Move left")
    elif row < trow:
        print("Move down")
    elif row > trow:
        print("Move up")

    