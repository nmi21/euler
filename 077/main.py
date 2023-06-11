"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

---
Method:
-

"""

import time
t = time.time()

# set the end target (the number we will count up to)
TARGET = 100


def sieve(n):
    out = [True] * (n+1)
    out[0] = False
    out[1] = False

    for i in range(2, n):
        if out[i]:
            j = i + i
            while j <= n:
                out[j] = False
                j += i

    return out


def calc_primes(n):
    matrix = sieve(n)
    return [i for i in range(len(matrix)) if matrix[i]]


# assume a sufficiently large number for calculations
TARGET = 100


# create an array called "ways" representing the number of ways that index, i, can be summed
ways = [0] * (TARGET + 1)
ways[0] = 1     # set 0 to 1 because you can only reach it 1 way --> not having anything

primes = calc_primes(TARGET)

for prime in primes:                        # iterate over the primes
    for j in range(prime, TARGET + 1):      # iterate over all the indices of ways
        ways[j] += ways[j - prime]

ans = 0
threshold = 5000
for i in range(len(ways)):
    if ways[i] >= threshold:
        ans = i
        break

print(ways)
print(i)
print(f"{time.time() - t} sec")

