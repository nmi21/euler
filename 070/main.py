"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers
less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

---
Method:
- get the totients for all values up to 10^7

"""
LIMIT = 10 ** 7


def phi(n: int):
    """
    returns the totient function phi(n)
    :param n:
    :return:
    """

    if n < 1:
        return 1

    prime_factors = get_prime_factors(n)
    res = n
    for prime in prime_factors:
        res *= 1 - (1 / prime)

    return int(res)


def get_prime_factors(num):

    n = num

    prime_factors = []

    # check to see if 2 is a prime factor
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2
        prime_factors.append(2)

    # check against all odd numbers up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            while n % i == 0:
                n = n // i
        i += 2

    # if n > 2, then n is a prime number
    if n > 2:
        prime_factors.append(n)

    return prime_factors


def is_permutation(s1, s2):
    str1 = sorted(str(s1))
    str2 = sorted(str(s2))
    if str1 == str2:
        return True
    else:
        return False

min_phi_ratio = 100
val_n = 0
for n in range(2, LIMIT):
    if n % 500000 == 0:
        print(f"checking {n}...")
    p = phi(n)
    if is_permutation(n, p) and n/p < min_phi_ratio:
        min_phi_ratio = n/p
        val_n = n
        print(f"__new min: {n} ({min_phi_ratio})")



