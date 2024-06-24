"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i)
each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from itertools import combinations, permutations, product


def sieve_of_eratosthenes(limit):
    sieve = [True for i in range(limit + 1)]
    sieve[0] = False
    sieve[1] = False
    n = 2
    while n <= limit:
        if sieve[n]:
            for i in range(n+n, limit + 1, n):
                sieve[i] = False
        n += 1
    primes = []
    for ind, ele in enumerate(sieve):
        if ele:
            primes.append(ind)
    return primes


# find the large primes that have the same numbers
def perms(num):
    num = str(num)
    p = list(permutations(num))
    ans = []
    for a in p:
        s = ""
        for b in a:
            s += b
        s = int(s)
        if s >= 1000:
            ans.append(s)
    ans = [*set(ans)]
    ans.sort()
    return ans



limit = 10000
primes = sieve_of_eratosthenes(limit)
# print(primes)
large_primes = [i for i in primes if i > 999]


primes_dict = {}
for prime in large_primes:
    combos = perms(prime)
    prime_combos = [c for c in combos if c in large_primes]
    if len(prime_combos) > 2:
        primes_dict[prime] = prime_combos

# print(primes_dict)


# TODO make a function that takes in a list
def combo_diffs(combo_list):
    # TODO function creates all combinations from the list in order, 3 terms
    l = list(combinations(combo_list, 3))
    ans = None
    for t in l:
        # TODO function takes difference from all combinations
        if t[2] - t[1] == t[1] - t[0]:
            # TODO function saves combination if the differences are equal
            ans = t
    return ans


ans = []
for prime in primes_dict:
    cond = combo_diffs(primes_dict[prime])
    if cond:
        ans.append(cond)

ans = [*set(ans)]


for tup in ans:
    if tup[0] == 1487:
        ans.remove(tup)

s = ""
for i in ans[0]:
    s += str(i)

print(s)






