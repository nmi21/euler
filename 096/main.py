"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a 
similar, and much more difficult, puzzle idea called Latin Squares. The objective of 
Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such 
that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an 
example of a typical starting puzzle grid and its solution grid.

    Unsolved
    0 0 3   0 2 0   6 0 0
    9 0 0   3 0 5   0 0 1
    0 0 1   8 0 6   4 0 0 

    0 0 8   1 0 2   9 0 0 
    7 0 0   0 0 0   0 0 8
    0 0 6   7 0 8   2 0 0 

    0 0 2   6 0 9   5 0 0 
    8 0 0   2 0 3   0 0 9
    0 0 5   0 1 0   3 0 0 

    Solved
    4 8 3   9 2 1   6 5 7
    9 6 7   3 4 5   8 2 1
    2 5 1   8 7 6   4 9 3

    5 4 8   1 3 2   9 7 6
    7 2 9   5 6 4   1 3 8
    1 3 6   7 9 8   2 4 5

    3 7 2   6 8 9   5 1 4
    8 1 4   2 5 3   7 6 9
    6 9 5   4 1 7   3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, 
although it may be necessary to employ "guess and test" methods in order to eliminate 
options (there is much contested opinion over this). The complexity of the search 
determines the difficulty of the puzzle; the example above is considered easy because 
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty 
different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first 
puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left 
corner of each solution grid; for example, 483 is the 3-digit number found in the top left 
corner of the solution grid above.

--

Method: 
- First, extract all of the puzzles
- For each puzzle, solve it

- How to solve sudoku
    - for each puzzle, make a "solved" copy
    - place each non zero number into the copy at the correct location
    - create a set for each unsolved location
    - remove from set illegals from each row, column, and box

- it appears that only 12 of the puzzles can be solved without guess and check
- need a new method

- Implement depth first search


"""


import time
import numpy
import os
import itertools

t = time.time()


def extract_puzzles():
    # grab the file path
    location = os.path.dirname(__file__)
    file_name = "p096_sudoku.txt"
    file_location = location + "/" + file_name

    # create an empty list and fill it with blocks of puzzles
    puzzles = []

    with open(file=file_location, mode="r") as file:

        # create an empty block to put sudoku lines into
        current_puzzles = []

        # check each line in the file to see if it contains "grid" (cast to lower case)
        # if it does, 
        for line in file:
            if "grid" in line.lower():
                if current_puzzles:
                    puzzles.append(current_puzzles)
                    current_puzzles = []
            else:
                num_list = [int(x) for x in line.strip()]
                current_puzzles.append(num_list)
        
        # add the last puzzle
        if current_puzzles:
            puzzles.append(current_puzzles)
        
    return puzzles


def is_move_valid(board, num, row, col):
    """
    Check if a "num" entered into "board" at "(row, col)" is valid:
    - num not in row
    - num not in col
    - num not in box
    """
    
    # check if valid in row
    if num in board[row]:
        return False
    
    # check if valid in col
    if num in [r[col] for r in board]:
        return False
    
    # check if valid in box (3x3 subportion)
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for r in range(3):
        for c in range(3):
            if num == board[start_row + r][start_col + c]:
                return False
    
    return True


def find_empty_cell(board):
    """
    Go through row by row and determine if an empty cell exists.
    """
    for r, c in itertools.product(range(9), repeat=2):
        if board[r][c] == 0:
            return r, c
    
    # else return None to indicate all solutions are filled
    return None, None


def solve_sudoku(board):
    
    # find next empty cell
    row, col = find_empty_cell(board)
    
    # if no empty cells, puzzle is complete!
    if row is None:
        return True
    
    # go across range 1-9
    for n in range(1, 9+1):
        # determine if move is valid
        if is_move_valid(board, n, row, col):
            
            # assign num to the move
            board[row][col] = n
    
            # recursion into the next step; return True if complete
            if solve_sudoku(board):
                return True
            
            # else it will be invalid, need to return num to 0
            board[row][col] = 0
    
    # backtrack by returning False; will then reassign board[row][col] to zero
    return False


unsolved_puzzles = extract_puzzles()

counter = 0
for unsolved_puzzle in unsolved_puzzles:
    puzzle = unsolved_puzzle
    solve_sudoku(puzzle)

    # add the first three numbers
    sudoku_num = int("".join([str(x) for x in puzzle[0][:3]]))
    counter += sudoku_num

ans = counter

print(f"{ans=}")

print(f"{time.time() - t} sec")
