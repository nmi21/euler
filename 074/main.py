"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out
that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

---
Method:
- go through every number from 1 to 1000000 to see if the chain == 60
- develop a function that creates a chain
    - start with the starting number and continue to add digit factorial sums until you find a number already in chain
- develop a function that turns a digit into the sum of the factorial of its digits
    - calculate the digit factorials outside of the function so that they aren't being calculated on every call

"""

import math

DESIRED_CHAIN_LENGTH = 60
LIMIT = 1000000

FACTORIAL_DIGITS = []
for i in range(10):
    FACTORIAL_DIGITS.append(math.factorial(i))


def factorial_digit_sum(num: int):
    num_str = str(num)
    sum = 0
    for j in num_str:
        sum += FACTORIAL_DIGITS[int(j)]
    return sum


def chain_length(start_num: int):
    num_list = [start_num]
    next_num = factorial_digit_sum(start_num)
    while next_num not in num_list:
        num_list.append(next_num)
        next_num = factorial_digit_sum(next_num)
    return len(num_list)


counter = 0
for i in range(1, LIMIT):
    if chain_length(i) == DESIRED_CHAIN_LENGTH:
        counter += 1

ans = counter
print(f"ans == {ans}")
