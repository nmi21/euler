"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

---

How to reduce search space:
- note that a pandigital in this form must satisfy the following:
    len(str(x) + str(y) + str(x*y)) == 9
- or other written:
    len(x) + len(y) + len(x*y) == 9
- thus, if len(x) == 1, then len(y) must be 4
- if len(x) == 2, then len(y) == 3
- if len(x) == 3, then len(y) == 2
- if len(x) == 4, then len(y) == 1
- we can ignore if len(x) is 3 or 4, because those effectively are the reverse of len(x) == 1 and 2, respectively
"""

from itertools import product

# write a function to check if num is pandigital
def is_pandigital(*args):
    num = [str(x) for x in list(args)]
    num = ''.join(num)
    if len(num) == 9 and set(num) == set("123456789"):
        return True
    return False


pan_prods = []
# first check over len(x) == 1; thus len(y) == 4
for x in range(1, 10):
    for y in range(1000, 10000):
        if is_pandigital(x, y, x*y):
            pan_prods.append([x, y, x*y])
            # print(pan_prods)

# then check over len(x) == 2; thus len(y) == 3
for x in range(10, 100):
    for y in range(100, 1000):
        if is_pandigital(x, y, x*y):
            pan_prods.append([x, y, x*y])
            # print(pan_prods)

# extract just the products
print(pan_prods)
prods = []
[prods.append(x[2]) for x in pan_prods if x[2] not in prods]
print(prods)

ans = sum(prods)
print(f"ans == {ans}")