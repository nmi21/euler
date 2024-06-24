"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

---
Method:
- Farey sequence
    - length given by 1 + PHI(n)
    https://en.wikipedia.org/wiki/Farey_sequence#Sequence_length_and_index_of_a_fraction
- PHI(n) is a summation of all totients from 1 to n
- to find totients efficiently, need to know first prime factor of each number 2:n
    - a method for calculating the totients can be found in totient_array
"""


def sieve_of_eratosthenes(size):
    sieve = [True] * (size + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, size + 1):
        if sieve[i]:
            for j in range(2*i, size + 1, i):
                sieve[j] = False

    primes = [ind for ind, ele in enumerate(sieve) if ele]

    return primes


def smallest_prime_factors(size):
    """
    return an array where the kth element is the smallest prime factor of k
    """
    primes = sieve_of_eratosthenes(size)
    Lp = [0] * (size + 1)
    Lp[0] = Lp[1] = 1

    # set the lowest prime factor of primes as the prime itself
    for prime in primes:
        Lp[prime] = prime

    # assign all even numbers because those are easy
    for i in range(2, size+1, 2):
        Lp[i] = 2

    # go through all other numbers and try all numbers <= number from primes to see if it is a factor
    for i in range(3, size + 1, 2):
        for prime in primes:
            if Lp[i] or i < prime:
                break
            if i % prime == 0:
                Lp[i] = prime
                break

    return Lp


def totient_array(size):
    """
    :return: phi; an array of length (size+1) where phi(k) is the totient value for k
    :param size: determines size of output array phi

    The totient function, phi, is given in its general form as follows
        phi(n) = n * PI{p|n}[ (1 - 1/p) ] where p are the prime divisors of n
    From this, it follows that if n is prime, then the only value of p that divides into n is when p == n
        Thus,
        phi(n) = n * PI{p|n}[ (1 - 1/p) ]
        phi(n) = n * (1 - 1/p)      NOTE: there is only one divisor, and there only one term p == n
        phi(n) = n * (1 - 1/n)
        phi(n) = n - n/n
        phi(n) = n - 1
    If n is not prime, then n is a composite number
        Let x be the smallest prime factor of n.
            if x and y are coprime, then
                it can be proven that phi(x*y) = phi(x) * phi(y)
            if x and y are not coprime, then
                we know that y has a factor of x (that is y % x == 0)
                phi(n) = n * PI{p|n}[ (1 - 1/p) ]
                phi(n) = x * y * PI{p|n} [ (1 - 1/p) ]
                since y % x == 0,
                    phi(y) = y * PI{p|n}[ (1 - 1/p) ]
                thus
                    phi(n) = x * phi(y) iff n = x*y and y % x == 0
    """

    primes = sieve_of_eratosthenes(size)
    Lp = smallest_prime_factors(size)

    phi = [0] * (size+1)
    phi[1] = 1

    for prime in primes:
        phi[prime] = prime - 1

    for k in range(2, size+1):
        # only do something if k is not prime
        if not phi[k]:
            x = Lp[k]
            y = k // x
            if y % x == 0:
                phi[k] = x * phi[y]
            else:
                phi[k] = phi[x] * phi[y]

    return phi


def farey_length(n):
    """
    |Fn| = 1 + PHI(n)
    PHI(n) is the summatory totient defined by
        PHI(n) = SIGMA(k=1, n) [phi(n)]
    """

    return 1 + sum(totient_array(n)[1:])


# Note that the Farey sequence includes the terms 0/1 and 1/1, but the projecteuler problem does not
# Therefore need to subtract 2 from the Farey sequence length to get the answer
d = 1000000
ans = farey_length(d) - 2
print(f"ans == {ans}")
