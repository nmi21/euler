"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


---

consider a 2x2 grid to have a pattern of 3x3 nodes:
    x   x   x
    x   x   x
    x   x   x
if we consider the solution to be how many ways we can get to the end (bottom right from each node), we can realize the
following to start:
    x   x   1
    x   x   1
    1   1   0
then, each x is how many ways we can get to the end from that node
each x can be calculated by adding its neighbors to the bottom and right
thus:
    x   x   1
    x   2   1
    1   1   0

    x   3   1
    3   2   1
    1   1   0

    6   3   1
    3   2   1
    1   1   0

If we want to expand to a 3x3 grid (4x4 node), we can add the extra spaces
    x   x   x   1
    x   6   3   1
    x   3   2   1
    1   1   1   0
then continue with the same addition style
    x   x   4   1
    x   6   3   1
    4   3   2   1
    1   1   1   0

    x   10  4   1
    10  6   3   1
    4   3   2   1
    1   1   1   0

    20  10  4   1
    10  6   3   1
    4   3   2   1
    1   1   1   0

Using the 3x3 node matrix again:
    6   3   1
    3   2   1
    1   1   0
If you invert the whole grid such that it looks like this:
    0   1   1
    1   2   3
    1   3   6
you can think of it as "how many possible paths to get to this location"
0,0 == 0 because it is the starting point
"""

import numpy as np
from itertools import product

# grid size m rows x n columns
m = 20
n = 20

arr = np.zeros((m + 1, n + 1), dtype=int)
# print(arr)

arr[0, :] = arr[:, 0] = 1
arr[0, 0] = 0
# print(arr)

for r, c in product(range(1, m+1), range(1, n+1)):
    arr[r, c] = arr[r-1, c] + arr[r, c-1]
    # print(arr)

print(arr)
ans = arr[m, n]
print(f"ans == {ans}")