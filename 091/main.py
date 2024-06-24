"""
This one is difficult to write out, and so please see the link:
https://projecteuler.net/problem=91

The points P(x1, y1) and Q(x2, y2) are plotted at integer coordinates
and are joined to the origin, O(0, 0), to form triangle(OPQ).

There are exactly fourteen triangles containing a right angle that can be formed
when each coordinate lies between 0 and 2 inclusive. 
That is, 
    0 <= x1, y1, x2, y2 <= 2

Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

--
Method: 
- iterate over all values for x1, etc.
- use A^2 + B^2 = C^2 to check if it is right triangle or not
"""

import math
import itertools
import time

t = time.time()


def distance_squared(p1: tuple, p2: tuple):
    # returns the linear distance between two points
    # points are given in (x, y) tuple format

    # decided not to use sqrt to be able to keep numbers in integer form and not have float errors

    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    delta_x = x2 - x1
    delta_y = y2 - y1

    return delta_x**2 + delta_y**2


def pythagorean_check_squares(a, b, c):
    # takes in three squared lengths from a triangle and determines if Pythagorean condition is met

    A, B, C = sorted([a, b, c])

    if A == 0 or B == 0 or C == 0:
        return False
    
    return A + B == C


def solve(limit):

    # create an empty list which will store right triangle coordinates
    right_tris = []

    # set the origin
    point_O = (0, 0)

    # iterate over all values of x1, etc.
    for x1, y1, x2, y2 in itertools.product(range(limit + 1), repeat=4):

        # if P and Q are both on the y axis, not a triangle
        if x1 == x2 == 0:
            continue

        # if P and Q are both on the x axis, not a triangle
        if y1 == y2 == 0:
            continue

        # compare the slopes
        if x1 == 0:
            slope1 = float('inf')
        else:
            slope1 = y1 / x1

        if x2 == 0:
            slope2 = float('inf')
        else:
            slope2 = y2 / x2

        if slope1 < slope2:
            continue

        # create the points
        point_P = (x1, y1)
        point_Q = (x2, y2)

        # grab the distances
        dist_OP = distance_squared(point_O, point_P)
        dist_OQ = distance_squared(point_O, point_Q)
        dist_PQ = distance_squared(point_P, point_Q)

        # see if the Pythagorean condition is met, add to the right tris list
        if pythagorean_check_squares(dist_OP, dist_OQ, dist_PQ):
            # points = sorted([point_P, point_Q])
            # right_tris.add(tuple(points))
            right_tris.append((point_P, point_Q))

    return right_tris


target = 50
ans = solve(target)

print(len(ans))
print(f"{time.time() - t} sec")
