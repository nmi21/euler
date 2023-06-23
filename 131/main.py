"""
There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + p*n^2
is a perfect cube.

For example, when
p = 19,
8^3 + 19*8^2 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only
four such primes below one-hundred.

How many primes below one million have this remarkable property?

--
We know:
n + p = x^3 / n^2
thus x^3 / n^2 must be an integer
and therefore n^2 must be a factor of x^3

Other constraints
p < 1,000,000
n < x

Forms of the equation:
n^3 + n^2 * p = x^3
p = (x^3 / n^2) - n
p = (x^3 - n^3) / n^2

Factor x^3 - n^3:
x^3 - n^3 = (x - n) * (x^2 + x*n + n^2)


This is interesting. Because it means that p = [(x - n) / n] * [(x^2 + x*n + n^2) / n]

Since the definition of a prime is that its only factors are 1 and itself, it must mean that:
[(x - n) / n] is a factor of p
[(x^2 + x*n + n^2) / n] is the other factor of p

Another way to look at the set of equations is:
n^3 + n^2 * p = x^3
n^3 * (1 + p/n) = x^3
n * (1 + p/n)^1/3 = x
From this... we know that if n and x are to be integers, then (1 + p/n)^1/3 must also be an integer
Rewrite it:
(1 + p/n) ^ 1/3
((n + p) / n) ^ 1/3     Let n+p = a^3; Let n = b^3
(a^3 / b^3) ^ 1/3
a / b is an integer

using Let n+p = a^3; Let n = b^3 :
p = a^3 - n     Let n = b^3
p = a^3 - b^3       Again we can use that expansion!
p = (a - b) * (a^2 + ab + b^2)

Again we have a-b and a^2 + ab + b^2 as factors of a prime number!
One of them must be == 1, and that is going to be a-b because we know that the numbers are all postive integers
a - b = 1
a = b + 1

Interestingly, the a and b are consecutive numbers!

So we can just continue to check all the numbers until the difference is above the limit.

Then compare that against a list of primes below the limit and see how many overlap!
"""

import time

t = time.time()


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(4, limit + 1, 2):
        sieve[i] = False

    for i in range(3, limit + 1, 2):
        if sieve[i]:
            for j in range(3 * i, limit + 1, 2 * i):
                sieve[j] = False

    return sieve


def get_primes(limit):
    sieve = sieve_of_eratosthenes(limit)
    primes = [x for x in range(len(sieve)) if sieve[x]]
    return primes


def get_cube_diffs(limit):
    def cube_diff(x):
        return x**3 - (x - 1)**3

    list_cube_diffs = []
    a = 2
    while cube_diff(a) < limit:
        list_cube_diffs.append(cube_diff(a))
        a += 1

    return list_cube_diffs


def solve(limit):
    # compare cube diffs against primes
    # there should be fewer cube diffs, and so we should go through those and iterate across while using set for primes

    c_diffs = get_cube_diffs(limit)
    primes = set(get_primes(limit))

    counter = 0
    for diff in c_diffs:
        if diff in primes:
            counter += 1

    return counter


limit = 10**6
# primes = get_primes(limit)
# c_diffs = get_cube_diffs(limit)

ans = solve(limit)
print(f"ans == {ans}")

print(f"{time.time() - t} sec")
