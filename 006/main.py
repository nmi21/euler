"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

limit = 100

sum_of_squares = sum([i ** 2 for i in range(1, limit + 1)])
square_of_sum = sum([i for i in range(1, limit + 1)]) ** 2

ans = square_of_sum - sum_of_squares
print(f"ans == {ans}")
