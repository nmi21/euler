"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^2 + 2^4
 
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

Method:
- Brute force

"""

import math
import time

t = time.time()

LIMIT = 50_000_000

def sieve_of_eratosthenes(size):
    sieve = [True] * (size + 1)
    sieve[0] = sieve[1] = False
    
    # remove evens except 2
    for i in range(4, size + 1, 2):
        sieve[i] = False

    # remove odds when it makes sense
    for j in range(3, size + 1, 2):
        if sieve[j]:
            for k in range(3*j, size + 1, 2*j):
                sieve[k] = False

    return sieve


def get_primes(limit):
    sieve = sieve_of_eratosthenes(limit)
    return [ind for ind, ele in enumerate(sieve) if ele]


# we would only ever need primes below square root of the limit
lim = int(math.sqrt(LIMIT)) + 1
primes = get_primes(lim)

sums = []
# a^2 + b^3 + c^4 <= LIMIT
for a in primes:
    for b in primes:
        for c in primes:
            s = a**2 + b**3 + c**4
            if s >= LIMIT:
                break
            sums.append(s)

ans = len(set(sums))
print(f"{ans=}")

print(f"{time.time() - t} sec")
