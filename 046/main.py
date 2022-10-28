"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""

from math import sqrt


def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for even in range(4, n + 1, 2):
        sieve[even] = False
    for i in range(3, n+1, 2):
        if sieve[i]:
            for j in range(2*i, n+1, i):
                sieve[j] = False
    return sieve


def get_primes(n):
    return [ind for ind, x in enumerate(sieve_of_eratosthenes(n)) if x]


def get_composite_odds(n):
    # again make a sieve, and initialize so that 0 and 1 are false
    comp_odds = [True] * (n+1)
    comp_odds[0] = comp_odds[1] = False

    # remove even numbers
    for i in range(2, n+1, 2):
        comp_odds[i] = False

    # now we have all odds, but need to change to numbers
    primes = get_primes(n)
    comp_odds = [ind for ind, x in enumerate(comp_odds) if comp_odds[ind] and ind not in primes]

    return comp_odds


# start with 10000 to see if we get anything; if not, increase the limit
lim = 10000

primes = get_primes(lim)
# print(f"primes == \n"
#       f"{primes}")
# print(len(primes))
# print()

comps = get_composite_odds(lim)
# print(f"comps == \n"
#       f"{comps}")
# print(len(comps))
# print()

double_squares = [2 * x ** 2 for x in range(1, int(sqrt(lim/2) + 1))]
# print(f"double_squares == \n"
#       f"{double_squares}")
# print(len(double_squares))
# print()

possible_sums = []
for prime in primes:
    for double_square in double_squares:
        x = prime + double_square
        if x % 2 != 0 and x < lim and x not in possible_sums:
            possible_sums.append(x)
possible_sums.sort()
# print(f"possible_sums == \n"
#       f"{possible_sums}")
# print(len(possible_sums))
# print()

ans = None
for comp in comps:
    if comp not in possible_sums:
        ans = comp
        break

print(f"ans == {ans}")

