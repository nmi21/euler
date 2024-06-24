"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

----

Method:
- write a prime factor solver
- extract only distinct factors
-


"""

from math import sqrt


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = int(n / 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = int(n / i)
    # else n is prime
    if n > 2:
        factors.append(n)
    return factors


def distinct_prime_factors(n):
    return [*set(prime_factors(n))]


def num_distincts(n):
    return len(distinct_prime_factors(n))


def check(n):
    return n == 4


n = 2
n_0 = num_distincts(n)
n_1 = num_distincts(n + 1)
n_2 = num_distincts(n + 2)
n_3 = num_distincts(n + 3)
while not (check(n_0) and check(n_1) and check(n_2) and check(n_3)):
    n += 1
    n_0 = n_1
    n_1 = n_2
    n_2 = n_3
    n_3 = num_distincts(n + 3)

ans = n
print(f"{n} = {distinct_prime_factors(n)}")
print(f"{n+1} = {distinct_prime_factors(n+1)}")
print(f"{n+2} = {distinct_prime_factors(n+2)}")
print(f"{n+3} = {distinct_prime_factors(n+3)}")
print()
print(f"ans == {ans}")



