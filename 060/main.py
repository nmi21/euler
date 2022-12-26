"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

---
Method:
- generate a list of all primes up to a limit
- take a subset of that list as the primes we want to compare
    - this should significantly reduce overall compute time
- create permutations for the list of numbers generated
- check each of the values from the permutations to see if it is in primes
    - if it is not in primes, continue to the next value

"""

SEARCH_LIMIT = 100_000_000
SUB_LIMIT = 10_000
FAMILY_SIZE = 4


def sieve_of_eratosthenes(size):
    sieve = [True] * (size + 1)
    sieve[0] = sieve[1] = False

    # eliminate all evens > 2
    for i in range(4, size + 1, 2):
        sieve[i] = False

    for i in range(3, size + 1, 2):
        if sieve[i]:
            for j in range(3*i, size + 1, 2*i):
                sieve[j] = False

    return sieve


def get_primes(limit):
    sieve = sieve_of_eratosthenes(limit)
    return [ind for ind, ele in enumerate(sieve) if ele]


primes = get_primes(SEARCH_LIMIT)
primes_strs = set([str(x) for x in primes])
sub_primes = [x for x in primes if x < SUB_LIMIT]


def check_perms(a, b):
    if str(a) + str(b) in primes_strs and str(b) + str(a) in primes_strs:
        return True
    return False


pair_sets = []
L = len(sub_primes)
s = 0
min_sum = SEARCH_LIMIT
for a in range(1, L):
    for b in range(a+1, L):
        p1 = primes[a]
        p2 = primes[b]
        s = p1 + p2
        if s > min_sum:
            break
        if not check_perms(p1, p2):
            continue
        for c in range(b+1, L):
            p3 = primes[c]
            s = p1 + p2 + p3
            if s > min_sum:
                break
            if not check_perms(p1, p3) or not check_perms(p2, p3):
                continue
            for d in range(c+1, L):
                p4 = primes[d]
                s = p1 + p2 + p3 + p4
                if s > min_sum:
                    break
                if not check_perms(p1, p4) or not check_perms(p2, p4) or not check_perms(p3, p4):
                    continue
                for e in range(d+1, L):
                    p5 = primes[e]
                    s = p1 + p2 + p3 + p4 + p5
                    if s > min_sum:
                        break
                    if not check_perms(p1, p5) or not check_perms(p2, p5) or not check_perms(p3, p5) or not check_perms(p4, p5):
                        continue
                    if s < min_sum:
                        min_sum = s
                        pair_sets.append([p1, p2, p3, p4])

print(f"ans == {min_sum}")
