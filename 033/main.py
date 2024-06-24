"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

---

Method: 
- check out the numbers from 10 - 99
- if a digit in the numerator is also in the denominator, remove the digit from both
- check if the fraction remains to be < 1
- check if the new fraction is equivalent to the old fraction
- if yes, store in a list
"""

from math import sqrt, prod


def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num = int(num / 2)
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = int(num / i)
    if num > 2:
        factors.append(num)
    return factors


def reduce_factors(numer, denom):
    n_factors = n_reduced_factors = prime_factors(numer)
    d_factors = d_reduced_factors = prime_factors(denom)
    for factor in n_factors[:]:
        if factor in d_factors:
            n_reduced_factors.remove(factor)
            d_reduced_factors.remove(factor)
    return n_reduced_factors, d_reduced_factors


def can_improper_reduce(n, d):
    # first determine if you can even reduce the number
    if str(n)[1] == str(d)[0]:
        n_reduced = int(str(n)[0])
        d_reduced = int(str(d)[1])
    else:
        return False

    # get the prime factors for n and d
    if reduce_factors(n, d) == reduce_factors(n_reduced, d_reduced):
        return True
    return False


fractions = []
for denom in range(10, 100):
    if denom % 10 == 0:
        continue
    for numer in range(10, denom):
        if numer % 10 == 0:
            continue
        if can_improper_reduce(numer, denom):
            fractions.append([numer, denom])

# print(fractions)

numerator = prod([x[0] for x in fractions])
denominator = prod([x[1] for x in fractions])
n_list, d_list = reduce_factors(numerator, denominator)

ans = prod(d_list)
print(f"ans == {ans}")
