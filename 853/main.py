"""
For every positive integer n the Fibonacci sequence modulo n is periodic.
The period depends on the value of n.
This period is called the Pisano period for n, often shorted to pi(n).

There are three values of n for which pi(n) equals 18: 19, 38, and 76.
The sum of the those smaller than 50 is 57.

Find the sum of the values of n smaller than 1,000,000,000 for which pi(n) equals 120.

--

Method:
- The Fibonacci sequence starts with [0, 1, 1], and because of that,
we know that it will repeat when it reaches [0, 1, 1] again
- Thus, we know that Fibonacci[120] % n will have to be 0
- We know that Fibonacci[120] % n == 0 when n is a factor of Fibonacci[120]
- We only have to check factors that are less than the limit (1,000,000,000)
- We need to then verify that the next two numbers are 1
- We finally need to remove any values for n where there exist multiple sequences
of [0, 1, 1] (e.g. when the period is a factor of 120)
"""

import time
import math
import itertools

t = time.time()


def get_fibonaccis(lim):
    """
    Gives a list of sequential fibonacci numbers starting with
    f0 = 0
    f1 = 1
    """

    fibonaccis = [0, 1]
    while len(fibonaccis) < lim + 3:
        fibonaccis.append(fibonaccis[-1] + fibonaccis[-2])
    
    return fibonaccis[: lim + 3]


def get_factors(num):
    """
    Returns a list of all factors of a number, num
    """

    # get the prime factors
    prime_factors = get_prime_factors(num)

    # make a list of lists for all of the possible exponents
    exponents = [[i for i in range(count + 1)] for count in prime_factors.values()]

    # create a tuple for each possible set of exponents
    exponent_combos = itertools.product(*exponents)

    # go through each exponent combo and create a new factor
    factors = []
    for exps in exponent_combos:
        factor = 1
        for p, e in zip(prime_factors.keys(), exps):
            factor *= p ** e
        factors.append(factor)
    factors.sort()

    return factors


def get_prime_factors(num):
    """
    Return a dictionary with prime factors of a number
    in the form
    dict = {
        a: x,
        b: y,
        c: z
    }

    where
        num = a^x * b^y * c^z
    """

    prime_factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            prime_factors.append(i)
            num = num // i
        if i > num:
            break
    
    factors_dict = {}
    for pf in prime_factors:
        factors_dict[pf] = factors_dict.get(pf, 0) + 1
    
    return factors_dict


def solve():

    # variables
    limit = 1_000_000_000
    n_max = 120

    # create fibonacci sequence
    fibs = get_fibonaccis(n_max)

    # we only care about factors less than the limit
    factors = [n for n in get_factors(fibs[n_max]) if n <= limit]

    # check all of the factors at elements n_max: n_max + 3
    potential_pisanos = []
    for f in factors:
        if [x % f for x in fibs[n_max: n_max + 3]] == [0, 1, 1]:
            potential_pisanos.append(f)

    # remove instances that have multiple repeats
    remove = []
    for pp in potential_pisanos:
        temp = [x % pp for x in fibs]

        # remove the beginning and ending [0, 1, 1]
        temp = temp[3:]
        temp = temp[:-3]

        # find zeros and check the next elements; remove that value
        for i in range(len(temp)):
            if temp[i] == 0 and temp[i+1] == temp[i+2] == 1:
                remove.append(pp)
                break
    for r in remove:
        potential_pisanos.remove(r)
    
    return sum(potential_pisanos)


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t} sec")
