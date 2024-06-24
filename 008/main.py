"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this
product?

"""

from number_block import num

LENGTH = 13


def string_prod(num_str):
    prod = 1
    for digit in num_str:
        prod *= int(digit)
    return prod


lines = num.split()
num = ""
for line in lines:
    num += line

max_prod = 0
for i in range(len(num) - LENGTH + 1):
    subset = num[i:(i+LENGTH)]
    if string_prod(subset) > max_prod:
        max_prod = string_prod(subset)

ans = max_prod
print(f"ans == {ans}")
