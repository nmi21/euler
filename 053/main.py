"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr.

In general,

nCr = n! / r!(n-r)!, where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23 choose 10 = 1144066
.

How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million?

---
Method:
Since we don't care if the result is the same as another...
- cycle over all n between 1:100 and r between 0:n
- if greater than limit, add 1 to counter

"""

from math import factorial


def comb(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


limit = 1000000
count = 0
for n in range(1, 100 + 1):
    for r in range(n):
        if comb(n, r) > limit:
            count += 1

ans = count
print(f"ans == {ans}")

