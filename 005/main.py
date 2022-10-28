"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

----

Method:
- get the prime factors for each value 1:20
- go through each prime factor and see who has the most for each factor
- take the most for each prime factor, and multiply all of those together
"""

limit = 20

# primes < 20
primes = [2, 3, 5, 7, 11, 13, 17, 19]

# TODO prime factorize each number
factors = []
for num in range(1, limit + 1):
    num_factors = []
    for prime in primes:
        while num % prime == 0:
            num_factors.append(prime)
            num = int(num / prime)
    factors.append(num_factors)

# find the most of each prime factor
primes_max = [0] * len(primes)
for i in range(len(primes)):
    for num in factors:
        if num.count(primes[i]) > primes_max[i]:
            primes_max[i] = num.count(primes[i])
print(primes_max)

# multiply all of those together
prod = 1
for i in range(len(primes)):
    prod *= primes[i] ** primes_max[i]

ans = prod
print(f"ans == {prod}")
