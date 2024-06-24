"""It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880...,
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots.
"""
import math
import time

t = time.time()

LIMIT = 100


def calc_int_sqrt(n):
    """
    We can solve this using Newton's method.

    https://stackoverflow.com/questions/15390807/integer-square-root-in-python
    """

    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def expand_num(num, digits):
    """
    To calculate the square root and not run out of precision, it should be in integer math.
    To do this, we would need to scale the sqrt by 10^n.
    Thus, we need to multiply the input number by the square of 10^n
        (10^n) ^ 2 = 10^2n
        
    e.g. expand 2 by 1 digit
    note: the sqrt of 2 is 1.4142135623730951...
    if we want to expand it 1 digit, we would need to take the sqrt of 200 as opposed to 20
    """
    return num * 10 ** (2 * digits)


def digital_sum(num):
    """
    Take the first 100 digits and sum
    """

    n = str(num)[:100]

    return sum(map(int, n))


def solve():
    # first 100 natural numbers; remove if a square
    nums = [x for x in range(1, LIMIT + 1) if int(math.sqrt(x)) ** 2 != x]

    # iterate over nums and add to sum
    s = 0
    for num in nums:
        s += digital_sum(calc_int_sqrt(expand_num(num, 100)))

    return s


ans = solve()
print(f"ans == {ans}")
print(f"{time.time() - t} sec")