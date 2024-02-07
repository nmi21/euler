"""
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in
the right column, and only moving up, down, and right, is indicated by (); the sum is equal to 994.

    131     673     (234)   (103)   (18)
    (201)   (96)    (342)   965     150
    630     803     746     422     111
    537     699     497     121     956
    805     732     524     37      331

Find the minimal path sum from the left column to the right column in matrix.txt (right click and
"Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.


---
Method:
- set the cost function for the leftmost column equal to itself
- set the cost function for each subsequent row by
    - First, add the value from the original matrix to the cost matrix from the left
    - Then, compare against the value from the original matrix + cost matrix below one cell
    - Finally, compare against the value from original matrix + cost matrix above one cell
- Grab the min value of the last column
"""

import os
import time

t = time.time()


my_data = [
    [131,     673,     234,     103,    18],
    [201,     96,      342,     965,    150],
    [630,     803,     746,     422,    111],
    [537,     699,     497,     121,    956],
    [805,     732,     524,     37,     331]
]


def min_path_sum(matrix, print_path_sum=0):
    # gets the minimal path sum of a matrix
    # matrix is given in the form:
    # matrix = [
    #   [x, x, x],
    #   [x, x, x],
    #   [x, x, x]
    # ]

    rows = len(matrix)
    cols = len(matrix[0])

    # create a 2D array to store the path sum
    path_sum = [[0] * cols for _ in range(rows)]

    # initialize the min path sum for the leftmost column
    # this will only be the value in that row, col
    for i in range(rows):
        path_sum[i][0] = matrix[i][0]

    # update the path for each subsequent column
    for j in range(1, cols):
        # consider three possibilities: 
        # 1. adding from the left
        # 2. adding from above
        # 3. adding from below

        # first consider adding from below, and initialize comparisons this way
        for i in range(rows):
            path_sum[i][j] = matrix[i][j] + path_sum[i][j - 1]

        # consider the values from above
        # note that the first row cannot have values from above, thus start at 1
        for i in range(1, rows):
            path_sum[i][j] = min(path_sum[i][j], matrix[i][j] + path_sum[i - 1][j])
        
        # finally, consider values when adding from the bottom
        # note that the last row cannot have values added from bottom,
        # thus...
        # 1. start at second to last
        # 2. go to row 0 (range --> -1)
        # 3. in steps of -1
        for i in range(rows - 2, -1, -1):
            path_sum[i][j] = min(path_sum[i][j], matrix[i][j] + path_sum[i + 1][j])

        if print_path_sum:
            print(f"{j=}")
            print(f"path_sum = [")
            for p in path_sum:
                print(f"    {p}")
            print("]")
            print()

    # from there, grab the min value from the last column
    return min([path_sum[i][-1] for i in range(rows)])


def extract_matrix():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_path = __location__ + "/" + "p082_matrix.txt"
    with open(file=file_path, mode="r") as file:
        # extract data from the file
        # remove leading and trailing whitespaces with .strip()
        # extract each element using .split() and select the , char to split on
        # map each element to an int
        # convert to a list
        # do it for each line in the file
        data = [list(map(int, line.strip().split(','))) for line in file]
    
    return data
    

mat = extract_matrix()
ans = min_path_sum(mat)

min_path_sum(my_data, print_path_sum=1)

print(f"{ans=}")
print(f"{time.time() - t} sec")
