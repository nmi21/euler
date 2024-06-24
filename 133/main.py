"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k
for exaemple, R(6) = 111111.

Let us consider repunits of the form R(10^n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10,000) is divisible by 17. Yet there is no value
of n for which R(10^n) will divide 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes
below one-hundred that can be a factor of R(10^n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10^n).

--
Method:
If a prime, p, is a factor of R(k), then:
    R(k) % p == 0               We know R(k) = (10^k - 1) / 9
    (10^k - 1) / 9 % p == 0
    10^k - 1 % 9*p == 0
    10^k % 9*p == 1             Let k = 10^n
    10^(10^n) % 9*p == 1
"""

import time

t = time.time()


def sieve_of_eratosthenes(n):
    """
    Create a sieve of all numbers from 0 through n.
    Returns a boolean array where sieve(n) returns True if n is prime, False if n is not prime.
    """

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # iterate over all evens except 2
    for i in range(4, n + 1, 2):
        sieve[i] = False

    # iterate over all odds
    for i in range(3, n + 1, 2):
        if sieve[i]:
            for j in range(3 * i, n + 1, 2 * i):
                sieve[j] = False

    return sieve


def get_primes(n):
    """
    Returns a list of all primes from 0 through n.
    """
    sieve = sieve_of_eratosthenes(n)
    return [i for i in range(len(sieve)) if sieve[i]]


def binary_modular_exponentiation(base, exponent, modulus):
    """
    A much more efficient version of modular_exponentiation.
    :param base:
    :param exponent:
    :param modulus:
    :return: (base ^ exponent) % modulus
    """
    if modulus == 1:
        return 0

    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result