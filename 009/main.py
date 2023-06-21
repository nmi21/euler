"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt


# prod = None
for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = sqrt(a**2 + b**2)
        if c - int(c) == 0 and a + b + c == 1000:
            # print(f"a == {a}, b == {b}, c == {int(c)}")
            prod = int(a*b*c)

ans = prod
print(f"ans == {ans}")