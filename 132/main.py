"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length (k).

For example, R(10) = 1111111111 = 11 x 41 x 271 x 9091,
and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).

--
Method / Notes:
- The number is obviously too large to realistically do anything with
- We could not conceivably do any sort of multiplication or division with it
- common methods of finding prime factors wouldn't really work because of how large the number is. I think in previous
problems, I ran into problems trying to find primes <= 10^20, and so never-mind trying to find something 10^9 long


--
See if there are any patterns.

Prime factors for different k values:
R(1)    :   1
R(2)    :   11
R(3)    :   3, 37
R(4)    :   11, 101
R(5)    :   41, 271
R(6)    :   5, 7, 11, 13, 37
R(7)    :   239, 4649
R(8)    :   11, 73, 101, 137
R(9)    :   3, 37, 333667
R(10)   :   11, 41, 271, 9091
R(11)   :   21649, 513239
R(12)   :   3, 7, 11, 13, 37, 101, 9901
These numbers were taken from Google searches.

The first thing that pops out is that R(k) contains all the prime factors from R(j) if j is a divisor of k.

E.g. R(12) --> k = 12 with divisors 2, 3, 4, 6
        R(12)   :   3, 7, 11, 13, 37, 101, 9901
        R(2)    :   11
        R(3)    :   3, 37
        R(4)    :   11, 101
        R(6)    :   5, 7, 11, 13, 37

There is typically another factor or two that is unaccounted for in this method. E.g. R(12) also contains 9901.
Perhaps given that we only need to sum the first 40 prime factors of R(10^9), it is possible that we don't need to
worry too much about those remainders.

--
Another observation is that you can begin to break down some of the numbers, which may be on the way to showing why the
previous method works.

R(10) = 1111111111
The divisors of 10 are 2 and 5. R(2) and R(5) are relatively easy to find the prime factors for.

R(10) = 1111111111 = 1111100000 + 11111 = R(5) * 10^5 + R(5)
    = R(5) * (10^5 + 1) = R(5) * 100001

R(10) = 1111111111 = 1100000000 + 11000000 + 110000 + 1100 + 11
    = R(2) * (10^8 + 10^6 + 10^4 + 10^2 + 1) = R(2) * 101010101

In this way, you could check for prime factors of 100001 and 101010101, but you could first divide out the prime factors
from R(2) and R(5), respectively.

Mathematically, if k is divisible by n, then R(k) can be represented in the following way:
    R(k) = R(n) * (10^n + 10^n-1 + 10^n-2 + ... + 10^n-n)           Note: 10^n-n == 10^0 == 1

Unfortunately, I think that this problem also becomes unsustainable very quickly. Even at relatively low values of
R(20), the  numbers would be challenging to find prime factors for.
    E.g. R(20) = R(10) * (10^10 + 1)
                    = R(10) * 10000000001

--
R(k)        Decimal         Difference: R(k) - R(k-1)
-----------------------------------------------------
R(1)    =            1  :   n/a
R(2)    =           11  :   10
R(3)    =          111  :   100
R(4)    =         1111  :   1000
R(5)    =        11111  :   10000
R(6)    =       111111  :   100000
R(7)    =      1111111  :   1000000
R(8)    =     11111111  :   10000000
R(9)    =    111111111  :   100000000
R(10)   =   1111111111  :   1000000000

So that tells me that the sequence R(k) follows a power law.

R(k) will always have k digits. So R(k) >= 10^(k-1) and R(k) < 10^k.
R(k) = (10^k - 1) / 9

--
At this point, we can use some modulus math!

Prime numbers mean that if you have a prime number, p, that is a prime factor of a number, n, then:
    n % p == 0
In this case, substitute n for R(k)
    R(k) % p == 0
Substitute for R(k)
    (10^k - 1) / 9 % p == 0
Then some mod math
    10^k - 1 % 9*p == 0
    10^k % 9*p == 1

To write that in a more mathy way:
    (10^k - 1) / 9 = 0 mod p
    10^k - 1 = 0 mod 9*p
    10^k = 1 mod 9*p

So really, all we have to solve is the first 40 values that that equation is satisfied!
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


# Give that our max number is 10^9, we can likely solve our sieve to be up to that number
# 10 ** 6 gives 78498 primes in 0.16 seconds using a sieve
# 10 ** 7 gives 664579 primes in 1.94 seconds using a sieve
# 10 ** 8 gives 5761455 primes in 20.99 seconds using a sieve
# 10 ** 9 gives 50847534 primes in 230.59 seconds using a sieve
# So, using a sieve may not actually be fast enough if the first 40 primes aren't <= 10**8

# start with 10**6
primes = get_primes(10 ** 6)


def generate_repunit(k):
    return ((10 ** k) - 1) // 9


def repunit_prime_factor(k, p):
    """
    :param k: repunit of form R(k)
    :param p: prime number p
    :return: Boolean; if R(k) % p == 0
    """
    # return (10 ** k) % (9 * p) == 1
    # This method seemed to bog down as values for k got even slightly large
    # Thus, need a more efficient algorithm
    base = 10
    exponent = k
    modulus = 9 * p
    return binary_modular_exponentiation(base, exponent, modulus) == 1


def modular_exponentiation(base, exponent, modulus):
    """
    Requires O(exponent) multiplications to complete.
    :param base:
    :param exponent:
    :param modulus:
    :return: (base ^ exponent) % modulus
    """
    # Based on https://en.wikipedia.org/wiki/Modular_exponentiation

    if modulus == 1:
        return 0

    c = 1
    for e_prime in range(exponent):
        # print(f"e' = {e_prime}. c = ({c} x {base}) mod {modulus} = {c * base} mod {modulus} = {(c * base) % modulus}")
        c = (c * base) % modulus

    return c


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


def repunit_prime_factor_generator(k, max_prime_factors=40):
    """
    Generates a list of prime factors for a repunit
    :param k: the repunit of the form R(k)
    :param max_prime_factors: max length of the list
    :return: list of prime factors
    """

    prime_factors = []
    for p in primes:
        if repunit_prime_factor(k, p):
            prime_factors.append(p)
            # print(f"Adding {p}...")
            if len(prime_factors) >= max_prime_factors:
                break

    return prime_factors


def solve(k, max_prime_factors=40):
    """
    :param k: repunit in form R(k)
    :param max_prime_factors: max number of prime factors to be considered
    :return: sum of all of the prime factors
    """
    res = repunit_prime_factor_generator(k, max_prime_factors)
    # print(res)
    # print(len(res))

    return sum(res)


k = 10 ** 9

ans = solve(k)
print(f"ans == {ans}")
print(f"{time.time() - t} sec")
