"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


from itertools import combinations, permutations


LIMIT = 1000000


# find all prime numbers below limit
def sieve_of_eratosthenes(num):
    """
    Efficient algorithm to calculate all prime numbers below a max_num

    :param num: maximum number to be calculated to, not inclusive
    :return: a list of all primes below max_num
    """
    sieve = [True for i in range(num)]
    sieve[0] = sieve[1] = False
    i = 2
    while i * i < num:
        if sieve[i]:
            for j in range(i * i, num, i):
                sieve[j] = False
        i += 1
    primes = [x for x in range(num) if sieve[x]]
    return primes


def rotate(num):
    num = str(num)
    left = num[0]
    right = num[1:len(num)]
    return int(right + left)


def circular_list(num):
    out = []
    iters = range(len(str(num)))
    for _ in iters:
        out.append(num)
        num = rotate(num)
    return out


primes = sieve_of_eratosthenes(LIMIT)
# print(primes)
print(f"len_primes = {len(primes)}")
# print()

# determine if the number is possibly circular
# for all numbers > 2, it cannot contain any even numbers else it will have an even permutation
evens = [str(d) for d in [0, 2, 4, 6, 8]]
subset_primes = []
for prime in primes:
    s_prime = str(prime)
    if prime > 2 and any(c in evens for c in s_prime):
        continue
    # for all numbers > 5, it cannot contain 5 else it will have a permutation divisible by 5
    if prime > 5 and '5' in s_prime:
        continue
    subset_primes.append(prime)

# print(subset_primes)
print(f"len_subset == {len(subset_primes)}")
# print()

circular = []
for prime in subset_primes:
    rotations = circular_list(prime)
    if all(num in subset_primes for num in rotations):
        circular.append(prime)

ans = len(circular)
print(f"ans == {ans}")
