# Sudoku Solver with Backtracking
'''
Sudoku puzzle:
Sudoku = [ 
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
'''
import numpy as np

Sudoku = [ 
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
    ]

# print(np.matrix(Sudoku))

# Checking the 'x' rows and 'y' columns for a possible number 'n'
# 'x' and 'y' range from 0 to 8 (inclusive) and 'n' ranges from 0 to 0 (inclusive)
def possibleNum(x, y, n):

    # Checking Rows and Columns for 'n'
    for i in range(0, 9):
        # Checking the row first
        if Sudoku[x][i] == n:
            return False
        # Checking the column next
        elif Sudoku[i][y] == n:
            return False

    # Checking the 3x3 square for 'n'
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if Sudoku[x0 + i][y0 + j] == n:
                return False
    return True

# print(possibleNum(4, 4, 6))

def solve():
    for x in range(9):
        for y in range(9):
            if Sudoku[x][y] == 0:
                for n in range(1, 10):
                    eval = possibleNum(x, y, n)
                    if eval == True:
                        Sudoku[x][y] = n
                        solve()
                        Sudoku[x][y] = 0
                return
    print(np.matrix(Sudoku))
    input("Press Enter if you want another solution!")

solve()