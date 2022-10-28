"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

LIMIT = 2000000


# create a sieve
def sieve_of_eratosthenes(limit):
    limit += 1
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for even in range(4, limit, 2):
        sieve[even] = False
    for i in range(3, limit, 2):
        if sieve[i]:
            for j in range(3*i, limit, 2*i):
                sieve[j] = False
    return sieve


# extract primes from sieve
def get_primes(limit):
    return [ind for ind, ele in enumerate(sieve_of_eratosthenes(limit)) if ele]


# sum primes
ans = sum(get_primes(LIMIT))
print(f"ans == {ans}")
