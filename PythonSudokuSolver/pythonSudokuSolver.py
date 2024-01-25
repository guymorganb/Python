def solveSudoku(board):
    emptyCell = findEmptyCell(board)
    
    if emptyCell is None:
        # All cells are filled, puzzle is solved
        return True
    
    row, col = emptyCell
    
    for num in range(1, 10):
        if isValidMove(board, row, col, num):
            board[row][col] = num
            
            if solveSudoku(board):
                return True
            
            board[row][col] = 0
    
    return False

def findEmptyCell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    
    return None

def isValidMove(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check subgrid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    
    return True

# Example puzzle
puzzle = [
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 8, 0, 0, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]
]

if solveSudoku(puzzle):
    for row in puzzle:
        print(row)
else:
    print("No solution found.")

#Note that the solver uses a backtracking algorithm to solve the puzzle. The findEmptyCell function returns the coordinates of the first empty cell it encounters, and the isValidMove function checks whether it is valid to place a number in a given cell.