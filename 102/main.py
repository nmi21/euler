"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle
is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.


---
Method:
- a method to determine if a point lies within the region of the triangle is to add the point in question (the origin)
to a set of points formed by the triangle. From there, determine the convex hull of the system.
    - if the hull has three points, then the point is within the triangle
    - if the hull has four points, then the point is outside of the triangle

- form the triangle with a vertices A, B, and C
    - let AB and AC be the vectors between A and the other two vertices
    - you can then give directions to the origin in terms of the vertex A and the two vectors AB and AC as follows:
        - origin = A + a*AB + b*AC
        where x and y are constants
    - solve for a and b to get:
        a = det(origin -- AC) - det(A -- AC) / det(AB -- AC)
        b = - (det(origin -- AB) - det(origin -- AB) / det(AB -- AC)

    where det(u -- v) == u x v == u_x * v_y - u_y * v_x


"""


def det(u, v):
    u_x = u[0]
    u_y = u[1]
    v_x = v[0]
    v_y = v[1]
    return (u_x * v_y) - (u_y * v_x)


def get_vectors(A, B, C):
    """
    From a triangle with vertices A, B, and C, return vectors v0, v1, and v2 where the following conditions are met:
    v0 = A
    v1 is the vector from A to B
    v2 is the vector from A to C
    """

    v0 = A
    v1 = (B[0] - A[0], B[1] - A[1])
    v2 = (C[0] - A[0], C[1] - A[1])

    return v0, v1, v2


def is_in_triangle(v, v0, v1, v2):
    a = (det(v, v2) - det(v0, v2)) / det(v1, v2)
    b = - (det(v, v1) - det(v0, v1)) / det(v1, v2)
    if a > 0 and b > 0 and a+b < 1:
        return True
    return False


def get_coords(coord_str):
    coords = coord_str.split(',')
    coords = [int(x) for x in coords]
    A = (coords[0], coords[1])
    B = (coords[2], coords[3])
    C = (coords[4], coords[5])
    return [A, B, C]


with open(file="p102_triangles.txt", mode="r") as f:
    tris = f.read().splitlines()

tris = [get_coords(tri) for tri in tris]
is_contained = []
num_contained = 0
v = (0, 0)
for tri in tris:
    A = tri[0]
    B = tri[1]
    C = tri[2]
    v0, v1, v2 = get_vectors(A, B, C)
    res = is_in_triangle(v, v0, v1, v2)
    is_contained.append(res)
    if res:
        num_contained += 1

ans = num_contained
print(f"ans == {ans}")
