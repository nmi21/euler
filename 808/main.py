"""
Both 169 and 961 are the square of a prime.
169 is the reverse of 961.

We call a number a reversible prime square if:
1. it is not a palindrome, and
2. it is the square of a prime
3. its reverse is also the square of a prime

169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.

-- 
- It seems that for the squares to be reversible, 
the primes also need to be reversible
    - so only use reversible primes
- pick some large number of primes to search through, and sort by
    - not a palindrome
    - reversible
"""

import time

t = time.time()


def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


def reverse_number(num):
    num_str = str(num)
    return int(num_str[::-1])


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit+1)
    sieve[0] = sieve[1] = False
    
    for i in range(4, limit+1, 2):
        sieve[i] = False
        
    for i in range(3, limit+1, 2):
        if sieve[i]:
            for j in range(3*i, limit+1, 2*i):
                sieve[j] = False
                
    return sieve


def get_primes(limit):
    return [ind for ind, ele in enumerate(sieve_of_eratosthenes(limit)) if ele]


def solve(lim=50_000_000):

    primes = get_primes(lim)
    prime_set = set(primes)

    # get all reversible primes
    rev_primes = [x for x in primes if reverse_number(x) in prime_set and x >= 10]

    # square the remaining primes and remove palindromes
    prime_sq = [x**2 for x in rev_primes if not is_palindrome(x)]
    prime_sq_set = set(prime_sq)

    rev_prime_sqs = [x for x in prime_sq if reverse_number(x) in prime_sq_set]

    if len(rev_prime_sqs) < 50:
        print(f"{len(rev_prime_sqs)=}")
        return None
    
    return sum(rev_prime_sqs[:50])


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t} sec")