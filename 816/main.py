"""
We create an array of points  in a two dimensional plane using the following random number generator:
s(0) = 290797
s(n+1) = s(n)^2 mod 50515093

P(n) = ( s(2n), s(2n+1) )

Let d(k) be the shortest distance of any two (distinct) points among P(0), ..., P(k-1).
E.g. d(14) = 546446.466846479

Find d(2,000,000). Give your answer rounded to 9 places after the decimal point.

---
Method:
- we likely can't brute force this
    - with 2,000,000 points, we would have (2000000)C(2) options
        - that is 2000000! / (1999998! * 2!)
        - or about 2,000,000,000,000
- similar to a quad tree (or perhaps even is a quadtree?)
- since we know that we are % 50515093, no number can be greater than that
- divide all the points into a grid system such that the grids are sufficiently small to only have a handful of points
- if we are to pick a point in the middle of the grid, it has 8 neighbors:
    x   x   x
    x   o   x
    x   x   x
- if we were to expand this to look at farther cells, it would look something like the following
    z   z   z   z   z
    z   x   x   x   z
    z   x   o   x   z
    z   x   x   x   z
    z   z   z   z   z
- this way, we can calculate the distances of all points within a single cell (use 'o' here) and determine the smallest
distance
- we know that the smallest distance cannot be in any 'z' cell so long as there are more than two points contained
within all 'x' and 'o' cells
- if we reduce the cell size such that there are sufficiently small numbers of points in each cell, this method becomes
very quick and effective
- some basic analysis of how many calculations we can expect
    - assume we divide into a 1000 x 1000 grid
    - assume points are equally distributed
    - this would mean that we would have 1,000,000 cells for 2,000,000 points
    - we would expect to see 2 points per cell
        - thus, we would only have to make 1 distance calculation for points within the cell for each cell
        - thus, we would expect to make 1,000,000 intra cell distance calculations
    - to check adjacent cells, we would have 8x adjacent cells
        - each cell we can assume has 2 points
        - this would mean that we would have to check 4 distances per adjacent cell
            - we do not need to check the distances within the cell
                - main point 1 and main point 2 distance has already been calculated
                - adjacent point 1 and adjacent point 2 distance will be calculated when evaluating that cell
            - so we check from main point 1 to adjacent point 1 and adjacent point 2
            - we also check from main point 2 to adjacent point 1 and adjacent point 2
        - at 4x distances per adjacent cell, 8 adjacent cells, and 1,000,000 cells (ignore boundaries)
            - we could expect to make 32,000,000 distance calculations
            - we can half this number by only forward propagating; that is, we don't need to calculate distances between
            adjacent cells if we have already done so in a previous step
            - so we would have a total of 16,000,000 distance calculations here
    - in total, we would expect on the order of 17,000,000 distance calculations, which should be relatively efficient

"""
import time
t = time.time()

D_LIMIT = 2_000_000
MOD_NUM = 50515093


# create a function that calculates Euclidean distance between two points
def dist(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


# generate all the values of s(n) necessary
s_list = [0] * (2 * D_LIMIT)
s_list[0] = 290797
for i in range(1, len(s_list)):
    s_list[i] = s_list[i-1]**2 % MOD_NUM

# create a dictionary that has a tuple cell reference for each key
num_divs = 1000
tree_dict = {}
for i in range(num_divs):
    for j in range(num_divs):
        tree_dict[(i, j)] = []

# generate all the points, and place them into the appropriate location within the dictionary
for p in range(D_LIMIT):
    x = s_list[2*p]
    y = s_list[2*p + 1]
    x_bin = x * num_divs // MOD_NUM
    y_bin = y * num_divs // MOD_NUM
    tree_dict[(x_bin, y_bin)].append((x, y))

# create our variables that we will track over time and change if we find a smaller distance
smallest_dist = float('inf')
# track some other info just for fun
smallest_point1 = None
smallest_point2 = None
longest_list = 0

# go through each element in each contained list (cell) and determine the smallest distance within that cell
for key in tree_dict:
    points_list = tree_dict[key]
    longest_list = max(longest_list, len(points_list))
    for i in range(len(points_list)):
        for j in range(i + 1, len(points_list)):
            d = dist(points_list[i], points_list[j])
            if d < smallest_dist:
                smallest_dist = d
                smallest_point1 = points_list[i]
                smallest_point2 = points_list[j]

# since we already calculated each cell, we only need to calculate adjacent ones
# if we start at (0,0), then go to (1,0), we only need to check the following:
#   - immediately to the right
#   - left down diagonal
#   - immediately down
#   - right down diagonal
# this should ensure that we cover each adjacent cell
# We don't have to calculate above at all nor to the immediate left because we would have already calculated that
# from a different cell
for i in range(num_divs):
    for j in range(num_divs - 1):
        # get the indices for all adjacent cells
        right = (i + 1, j)
        down_left = (i - 1, j + 1)
        down = (i, j + 1)
        down_right = (i + 1, j + 1)
        adjacent_cells = [right, down_left, down, down_right]

        # the current cell would just be (i, j)
        current_cell = (i, j)

        # start with each point in the current cell
        for pt1 in tree_dict[current_cell]:
            for cell in adjacent_cells:

                # check to make sure that cell indices are valid, otherwise skip
                if cell not in tree_dict:
                    continue

                # check against each point within the adjacent cell
                for pt2 in tree_dict[cell]:
                    d = dist(pt1, pt2)
                    if d < smallest_dist:
                        smallest_dist = d
                        smallest_point1 = pt1
                        smallest_point2 = pt2

ans = round(smallest_dist, 9)
print(f"ans == {ans}")

print(f"{time.time() - t} sec")
