"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Method:
- we know the number cannot be larger than 987654321
- so we can make a sieve up to and including that number
- then work backwards from list, and the first one we find that is pandigital is the largest

Old code:
# def sieve_of_eratosthenes(num):
#     sieve = [True] * (num + 1)
#     sieve[0] = sieve[1] = False
#     for even in range(4, num+1, 2):
#         sieve[even] = False
#     for i in range(3, num+1, 2):
#         if sieve[i]:
#             for j in range(3*i, num+1, 2*i):
#                 sieve[j] = False
#     return sieve
#
#
# def get_primes(num):
#     sieve = sieve_of_eratosthenes(num)
#     return [ind for ind, ele in enumerate(sieve) if ele]

It turns out that a sieve is efficient, but it requires a lot of memory that my computer apparently doesn't have
- thus, it seems like the best thing to do would be to get a list of all possible permutations of the numbers
- then check if each one is prime
- however, probably is more compute intensive because it means you have to check if each one is prime
- possible that the numbers don't fit in 123456789 pandigital, therefore need to check 12345678, 1234567, etc.
- this means that there are 9! + 8! + 7! + ... + 1! possibilities to check
"""

from math import sqrt
from itertools import permutations

max_num = "987654321"


def is_pandigital(num):
    pan_str = "123456789"
    pan_str = pan_str[0:len(str(num))]
    num = str(num)
    for digit in pan_str:
        if digit not in num:
            return False
    return True


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


max_pandigital_prime = None
for l in range(len(max_num)):
    # change the numbers that we are checking against
    limit = max_num[l:]

    # get all numbers as permutations of MAX_NUM
    perms = list(permutations(limit))
    perms = [int(''.join(tup)) for tup in perms]
    primes = [x for x in perms if is_prime(x)]
    if primes:
        max_pandigital_prime = max(primes)
    if max_pandigital_prime:
        break

ans = max_pandigital_prime
print(f"ans == {ans}")
