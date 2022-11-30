"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

---
Method:
- we know that the first term in a Farey sequence will be 0/1
- we know that for a Farey sequence F(n), the second term will be 1/n
- from this, we can determine all other terms using the formula from
    https://en.wikipedia.org/wiki/Farey_sequence#Next_term
- Given two consecutive fractions a/b and c/d in a sequence F(n), the next fraction p/q can be calculated as follows:
    p = ((n + b) // d) * c - a
    q = ((n + b) // d) * d - b
- Use the code from 071 to find the term just to the left of 1/3
- Then use the next term formula to generate the next term until you find 1/2, using a counter the whole time

"""
from fractions import Fraction

LIMIT = 12000

numer = 1
denom = 3
lowest_diff = Fraction(numer, denom)
lowest_n = None
lowest_d = None
for d in range(1, LIMIT + 1):

    n = numer * d // denom
    f = Fraction(n, d)

    if f == Fraction(numer, denom):
        f = Fraction(n-1, d)

    diff = Fraction(numer, denom) - f
    if diff < lowest_diff:
        lowest_diff = diff
        lowest_n = n
        lowest_d = d

n = LIMIT
a = lowest_n
b = lowest_d
c = 1
d = 3
counter = 0
while True:
    p = ((n + b) // d) * c - a
    q = ((n + b) // d) * d - b
    if q == 2:
        break
    counter += 1
    a, b, c, d = c, d, p, q

ans = counter
print(f"ans == {counter}")