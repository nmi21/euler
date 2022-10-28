"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

---
Method:
- start dividing out by prime numbers
- 2 is only even number, so we can start with that, and then start at 3, skip by two to reduce search space
    - there will be some overlap (e.g. 9, 15, 21) that could be avoided, but will only implement it if efficiency
    requires it

"""
from math import sqrt

NUMBER = 600851475143


def largest_prime_factor(num):
    # set the largest_factor
    largest_factor = None
    # first deal with 2 (only even prime)
    while num % 2 == 0:
        num = int(num/2)
        largest_factor = 2

    # at this point we know that we have removed all factors of 2 from num
    # any number can have at most 1 prime factor > sqrt(n); can keep reducing search space as we find more factors
    div = 3
    max_search = sqrt(num)
    while num > 1 and div < max_search:
        while num % div == 0:
            num = int(num / div)
            largest_factor = div
            max_search = sqrt(num)
        div += 2  # this way we only search odd numbers

    if num == 1:
        return largest_factor
    return num


ans = largest_prime_factor(NUMBER)
print(f"ans == {ans}")
