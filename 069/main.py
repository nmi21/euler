"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1	    2
3	1,2	                2	    1.5
4	1,3	                2	    2
5	1,2,3,4	            4	    1.25
6	1,5	                2	    3
7	1,2,3,4,5,6	        6	    1.1666...
8	1,3,5,7	            4	    2
9	1,2,4,5,7,8	        6	    1.5
10	1,3,7,9	            4	    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

---
Method:
- Euler's product formula: https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula
    - phi(n) = n * PI[p|n](1 - 1/p)
        that is the product (1 - 1/p) for all values of p that are prime factors of n, then all multiplied by n


"""

LIMIT = 1000000


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


totient_norms = [ x / phi(x) for x in range(LIMIT + 1) ]

ans = totient_norms.index(max(totient_norms))
print(f"ans == {ans}")



