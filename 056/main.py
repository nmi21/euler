"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

----

Method:
- create an a x b sized array, where each cell is a^b
- find the max value

"""

import numpy as np
from itertools import product


lim = 100
max_sum = 0
for a, b in product(range(lim), range(lim)):
    # if a % 10 == 0 and b % 10 == 0:
    #     print(f"a == {a}")
    #     print(f"b == {b}")
    #     print()

    prod = a ** b
    dig_sum = sum([int(x) for x in str(prod)])
    if dig_sum > max_sum:
        max_sum = dig_sum

ans = max_sum
print(f"ans == {ans}")
