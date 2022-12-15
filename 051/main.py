"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53,
73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently, 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

---
Method:
- We know that the answer must be > 10,000
    - if the prime only had 4 digits, there are only 6 possible ways to change it
    - therefore it wouldn't fit the requirements
- Develop a sieve to find all primes then truncate to values 10,000 < x < 1,000,000
    - this should give us a good search range
- additionally, we know that we cannot change the last number when we change the digits, because there are not enough
odd digits to be able to create prime numbers
    - so we can probably sort into 4 lists:
        - N % 10 == 1, 3, 7, 9
        (note: we will not have any primes that end in 5 after 5 itself
        (note: there are no even primes besides 2)
- since we know that we are replacing the numbers with the same digit, we can look for primes that have the same digit
in multiple locations

"""

SEARCH_LIMIT = 1_000_000
FAMILY_SIZE = 8


def sieve_of_eratosthenes(size):
    sieve = [True] * (size + 1)
    sieve[0] = sieve[1] = False

    # eliminate all evens > 2
    for i in range(4, size + 1, 2):
        sieve[i] = False

    for i in range(3, size + 1, 2):
        if sieve[i]:
            for j in range(2*i, size + 1, i):
                sieve[j] = False

    return sieve


def get_primes(limit):
    sieve = sieve_of_eratosthenes(limit)
    return [ind for ind, ele in enumerate(sieve) if ele]


def create_placeholder(s, ind):
    # will take in a string and replace the element at ind with a *
    return s[0:ind] + '*' + s[(ind + 1):]


def generate_wildcards(s, index, w_list):
    # if the index is > 0, then we know that we have inserted a * somewhere
    if index > 0:
        w_list.append(s)
    # only go to len(s) - 1 because we know we don't need to change the last number
    for x in range(index, len(s) - 1):
        # replace digit at index with *, move on to the next index, and pass in the list
        generate_wildcards(create_placeholder(s, x), x + 1, w_list)


# grab all primes below the search limit, and then create a set, which will be faster to check for inclusion
primes = [str(x) for x in get_primes(SEARCH_LIMIT)]
prime_set = set(primes)

# set flags to see if we can exit for loop
ans_found = False
ans = None
for prime in primes:

    # generate all possible wildcards for a given prime number
    wildcards = []
    generate_wildcards(prime, 0, wildcards)

    for wildcard in wildcards:
        # for each wildcard, create a list of numbers replacing the * with digits 0-9
        num_list = [wildcard.replace("*", str(x)) for x in range(0, 10)]
        # check to see if those numbers are in prime_set
        wild_primes = [x for x in num_list if x in prime_set]

        # see if we have eclipsed the prime number family set we are looking for; if yes, break out of loops
        if len(wild_primes) >= FAMILY_SIZE:
            ans_found = True
            ans = int(wild_primes[0])
            break

    if ans_found:
        break

print(f"ans == {ans}")
