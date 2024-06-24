"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If
this process is continued, what is the side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

---
Method:
- we know that n x n square is only valid if n is odd
- if n == 1, then there is only one value for one corner, which is 1
- otherwise, we can determine the values for the corner in the following ways:
    1. n**2
    2. n**2 - (n-1) = n**2 - n + 1
    3. n**2 - 2*(n-1) = n**2 - 2n + 2
    4. n**2 - 3*(n-1) = n**2 - 3n + 3
- we can add all values of the corners to a list everytime we increase the size of the square
- we can check if those values are prime, and then add them to a different list
- compare the lengths of the lists:
    - we want:
             primes < .1 * nums
             primes < nums / 10
        10 * primes < nums

"""

from math import sqrt

CORNER_NUMS = [1]
CORNER_PRIMES = []


# write a prime number checker
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


# TODO write a corner number generator
def add_corners():
    n = int(sqrt(CORNER_NUMS[-1])) + 2
    # print(n)
    c1 = n**2 - 3*n + 3
    c2 = n**2 - 2*n + 2
    c3 = n**2 - n + 1
    c4 = n**2
    CORNER_NUMS.append(c1)
    CORNER_NUMS.append(c2)
    CORNER_NUMS.append(c3)
    CORNER_NUMS.append(c4)


# TODO track primes that are being added
def add_primes_from_corners():
    for x in range(4):
        num = CORNER_NUMS[-1 - x]
        if is_prime(num):
            CORNER_PRIMES.append(num)


def expand_spiral():
    add_corners()
    add_primes_from_corners()


# initialize the spiral to be the same as the problem, currently n = 1
# expand to 3x3
expand_spiral()
# expand to 5x5
expand_spiral()
# expand to 7x7
expand_spiral()

while 10*len(CORNER_PRIMES) > len(CORNER_NUMS):
    expand_spiral()

n = int(sqrt(CORNER_NUMS[-1]))  # this is the length of the sides
# print(f"ratio == {len(CORNER_PRIMES) / len(CORNER_NUMS)}")

ans = n
print(f"ans == {ans}")

