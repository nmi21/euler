"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?


----
- we know that 10^n will always be greater than n digits:
    - 10^1 = 10 has 2 digits
    - 10^2 = 100 has 3 digits
    - in fact, it will always have n+1 digits
- as we ascend the values of n, we know that 9^n is the largest value that has the potential to be included
- as soon as 9^n has fewer than n digits, we have reached the upper limit of what is possible for those digits:
    10^(n-1) <= 9^n
    log10(10^(n-1)) <= log10(9^n)
    (n-1) * log10(10) <= n * log10(9)
    n - 1 <= n * log10(9)
    n - n*log10(9) - 1 <= 0
    n*(1 - log10(9)) - 1 <= 0
    n*(1 - log10(9)) <= 1
    n <= 1 / (1 - log10(9))


"""

import math
import itertools

limit_n = 1 / (1 - math.log10(9))
limit_n = int(limit_n)

n_power_digs = []
for n, x in itertools.product(range(1, limit_n), range(0, 10)):
    num = x ** n
    if n == len(str(num)):
        n_power_digs.append(num)

ans = len(n_power_digs)
print(f"ans == {ans}")
