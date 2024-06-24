"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from itertools import combinations


# create a factors solver
def determine_factors(n):
    factors = []
    for x in range(1, (n // 2) + 1):
        if n % x == 0:
            factors.append(x)
    return factors


def is_abundant(n):
    if (sum(determine_factors(n)) > n):
        return True
    return False


# if number is abundant, add to list
abund = []
stop = 28123
for x in range(1, stop + 1):
    if is_abundant(x):
        abund.append(x)
print(f"abund == {abund}")

# determine all combinations of numbers in the list and what the sums are
# combos needs to include if something is added to itself;
# it is not just unique abundant numbers that need to be summed
combos = list(combinations(abund + abund, 2))
# sums represents all of the sums in the combos
sums = [x[0] + x[1] for x in combos]
sums = list(set(sums)) # removes duplicates
print(f"sums == {sums}")
print(f"len sums == {len(sums)}")

# create a list of numbers 1:stop, add the sums, and then remove duplicates
# remainder should be numbers that cannot be represented as the sum of two abundant numbers
lim_range = list(range(1, stop + 1))
remainder = [x for x in lim_range if x not in sums]
print(f"remainder == {remainder}")
print(f"len remainder == {len(remainder)}")

# sum all of the remaining numbers
tot_sum = sum(remainder)
print(f"tot_sum == {tot_sum}")
