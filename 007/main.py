"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

limit = 10001


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


primes = []
i = 1
while len(primes) < limit + 1:
    if is_prime(i):
        primes.append(i)
    i += 1

ans = primes[-1]
print(f"ans == {ans}")
