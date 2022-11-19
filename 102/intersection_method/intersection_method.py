"""
attempt to solve 102 via intersection method (ray tracing)

---
Method:
- given that we know the extents of the allowable area, we can draw a ray from the origin in any direction and see if it
intersects the line segments formed by the three points
- for our system, we will start at the origin and draw a line to the extent of x == 1000
- for each pair of points, we will
    - determine the line equation y = m*x + b
    - determine where the line intersects the x-axis by setting y = 0\
    - verify that the intersection is in the region between 0 <= x <= 1000
    - verify that the intersection is in the values of x given by the two points
- for the special case where a segment is parallel to the x-axis, b must be 0 to satisfy the condition
"""
import time
t = time.time()

def get_coords(coord_str):
    coords = coord_str.split(',')
    coords = [int(x) for x in coords]
    A = (coords[0], coords[1])
    B = (coords[2], coords[3])
    C = (coords[4], coords[5])
    return A, B, C


def intersect_pos_x(pt1, pt2):
    pt1x = pt1[0]
    pt2x = pt2[0]
    if pt1x < 0 and pt2x < 0:
        return False

    run = pt2x - pt1x
    if run == 0:
        print("Vertical line!")
        if pt1x == 0:
            return True
        else:
            return False

    pt1y = pt1[1]
    pt2y = pt2[1]
    rise = pt2y - pt1y
    if rise == 0:
        if pt1y == 0:
            return True
        else:
            return False

    m = rise / run
    b = pt1y - m * pt1x

    x = -b / m
    left = min(pt1x, pt2x)
    right = max(pt1x, pt2x)

    if 0 <= x <= 1000 and left <= x <= right:
        return True
    else:
        return False


def includes_origin(triangle_pts):
    A, B, C = get_coords(triangle_pts)

    # the ray can only cross one line one time, if it is anything other than one intersection, it is outside the
    # triangle
    intersections = 0
    if intersect_pos_x(A, B):
        intersections += 1
    if intersect_pos_x(A, C):
        intersections += 1
    if intersect_pos_x(B, C):
        intersections += 1

    if intersections == 1:
        return True
    else:
        return False


with open(file="../p102_triangles.txt", mode="r") as f:
    data = f.read().splitlines()

has_origin = [includes_origin(tri) for tri in data]

ans = len([x for x in has_origin if x])
print(f"ans == {ans}")