"""
Consider the divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30 It can be seen that for every divisor d of 30, d + 30/d is prime.

Find the sym of all positive integers n not exceeding 100,000,000 such that for every divisor d of n, d + n/d is prime

--

The largest value of d + n/d is when n is large and d is small; 
so n --> LIMIT and d --> 1
at which point d + n/d = n+1

Find all primes <= n+1

For any pair of divisors such that d1 * d2 = n, we only have to check the d1 + n/d1 case
because d2 will return the same value. This will half our search space.

We only need to check up to the square root of the number because it will otherwise be taken care of by other divisors.
"""

import time
import math

t = time.time()

LIM = 100_000_000


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    # deal with evens > 2
    for i in range(4, limit + 1, 2):
        sieve[i] = False
        
    # deal with odds
    for i in range(3, limit + 1, 2):
        if sieve[i]:
            for j in range(3*i, limit + 1, 2*i):
                sieve[j] = False
                
    return sieve


def get_primes(limit):
    return set([ind for ind, ele in enumerate(sieve_of_eratosthenes(limit)) if ele])


def solve(limit=LIM):

    primes = get_primes(limit)

    def check_div_prime(num):
        """
        note that you only need to check 1/2 of the divisors:
        
        let d1 * d2 = n
        
        val1 = d1 + n/d1
        
        val2 = d2 + n/d2
        val2 = (n/d1) + n/(n/d1)
        val2 = n/d1 + d1
        val2 = d1 + n/d1
        val2 = val
        
        So, for any pair of divisors such that d1 * d2 = n,
        we only have to check the d1 + n/d1 case
        """
    
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if (i + num//i) not in primes:
                    return False
        
        return True

    res = 0
    for i in range(1, LIM+1):
        if check_div_prime(i):
            res += i

    return res


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t} sec")
