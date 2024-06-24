"""
Let D(n) be the n-th positive integer that has the sum of its digits a prime

For example, D(61) = 157 and D(10^8) = 403539364

Find D(10^16)

https://projecteuler.net/problem=845
"""

"""
First 10 values of D(n):
D(1) = 2
D(2) = 3
D(3) = 5
D(4) = 7
D(5) = 11
D(6) = 12
D(7) = 14
D(8) = 16
D(9) = 20
D(10) = 21
"""

"""
Method:
- 
"""

import math
import time

t = time.time()
LIMIT = 100


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


nums = list(range(1, LIMIT + 1))
primes = [x for x in range(150) if is_prime(x)]
primes = set(primes)


def digital_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


def next_d_of_n(d_n_minus_1=0):
    val = d_n_minus_1 + 1
    while digital_sum(val) not in primes:
        val += 1
    return val


def solve(n=10):
    Dn = next_d_of_n(0)
    for i in range(1, n+1):
        Dn = next_d_of_n(Dn)
    print(f"D(n) == D({i}) == {Dn}")


# print(nums)
# print(primes)
# solve(10 ** 8)


def counter(n):
    count = 0
    while count < n:
        count += 1
    return count


def digital_sum_patterns(start=0, end=10):
    for i in range(start, end+1):
        print(f"{i}: {digital_sum(i)}")


# digital_sum_patterns(1, 62)


# for i in range(1, 10):
#     print(f"Counter: {counter(10 ** i)}")


res = 0
for i in range(10**6):
    start = i * 100
    end = start + 99
    prime_sums = [x for x in range(start, end + 1) if digital_sum(x) in primes]
    res += len(prime_sums)
    print(f"start == {start}")
    print(f"end == {end}")
    print(f"total prime sums == {res}")
    print(prime_sums)
    print(len(prime_sums))
    print()

print(f"{time.time() - t} sec")