"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the
almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by
no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose
perimeters do not exceed one billion (1,000,000,000).

---
Method:
- going through the first 1,000,000 solutions via brute force takes approximately 1sec
- thus, going to 1,000,000,000 is going to take far longer than the 60sec alotted time
- brute force likely won't be able to solve it

- an isosceles triangle can be divided into two equal right triangles
- if the triangle has sides s1, s1, and s2, the two right triangles will have
    - hypotenuse == s1
    - leg = s2 / 2
    - leg = h (height of isosceles triangle as well)
- in order for the area of the triangle to be an integer solution, the height must be an integer
- if all of the sides are integers, then it is a Pythagorean triple!
- we can generate Pythagorean triples relatively easily
- not all Pythagorean triples will yield almost equilateral triangles
- only primitive Pythagorean triples will yield almost equilateral triangles

- generate primitive Pythagorean triples until the perimeter of two back to back cannot be smaller than 1,000,000,000
    - for the generator, m > n > 0
- check each triple to see if it will construct an almost equilateral triangle
- add all of the perimeters of those triangles
"""

import math
import time

t = time.time()


limit = 1_000_000_000

# create an empty list for triples
py_trips = []

total = 0
# set initial conditions
m = 2
while True:
    n = 1
    while n < m:
        # generate the triple
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        leg = min(a, b, c)
        hyp = max(a, b, c)

        if abs(2*leg - hyp) == 1:
            # you've found a valid triple for an almost equilateral triangle
            py_trips.append([hyp, hyp, 2*leg])
            total += 2*hyp + 2*leg

        n += 1

    perimeter = 2*hyp + 2*leg
    if perimeter > limit:
        break

    m += 1

for trip in py_trips:
    print(trip)

print()
print(f"{total=}")

print(f"{time.time() - t}sec")
