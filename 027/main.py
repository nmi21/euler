"""
Consider
n^2 + an + b, where |a| < 1000 and |b| <= 1000

find the product of the coefficients a and b for the quadratic that produces the maximum number of primes for
consecutives values of n, starting with n = 0
"""

import math
from itertools import product
from numpy import prod

# TODO search over the space indicated

# create a prime checker algorithm
def is_prime(num):
    if num < 1:
        return False
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    lim = math.sqrt(num)
    k = 5
    while k <= lim:
        if num % k == 0:
            return False
        if num % (k + 2) == 0:
            return False
        k += 6
    return True


# create a quadratic calculator
def quad(n, a, b):
    return n**2 + a*n + b


# create a consecutive values of n checker prior to prime
def n_checker(a, b):
    n = 0
    while is_prime(quad(n, a, b)):
        n += 1
    return n - 1


def num_range(num):
    return range(-num, num + 1)


a_lim = 1000 - 1
b_lim = 1000
a_range = num_range(a_lim)
b_range = num_range(b_lim)


n_max = 0
my_pair = []
for a, b in product(a_range, b_range):
    n = n_checker(a, b)
    if n > n_max:
        n_max = n
        my_pair = [a, b]


my_prod = prod(my_pair)

print(f"my_pair == {my_pair}")
print(f"n_max == {n_max}")
print(f"prod == {my_prod}")

