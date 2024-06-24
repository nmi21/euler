"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the
fraction immediately to the left of 3/7.

---
Method:
- cycle over all of values of denominator d from 1 to 1,000,000
- determine n by the formula 3*d // 7
- determine the difference between the fraction given by n/d and 3/7
    - if the difference is 0, have the fraction be n - 1 / d and recalculate
- if the difference is less than previous lowest difference, replace

"""

from fractions import Fraction

LIMIT = 1000000

numer = 3
denom = 7
lowest_diff = Fraction(numer, denom)
lowest_n = None
for d in range(1, LIMIT + 1):

    n = numer * d // denom
    f = Fraction(n, d)

    if f == Fraction(numer, denom):
        f = Fraction(n-1, d)

    diff = Fraction(numer, denom) - f
    if diff < lowest_diff:
        lowest_diff = diff
        lowest_n = n

ans = lowest_n
print(f"ans == {ans}")

