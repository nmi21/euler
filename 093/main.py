"""
By usingeach of the digits from the set, {1, 2, 3, 4}, exactly once,
and making use of the four arithmetic operations (+, -, x, /) and
brackets/parentheses, it is possible to form different positive integer targets.

For example,
    8 = (4 x (1 + 3)) / 2
    14 = (4 x (3 + 1/2))
    19 = 4 x (2 + 3) - 1
    36 = 3 x 4 x (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 
can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest
set of consecutive integers, 1 to n, can be obtained, giving your answer as
a string: abcd.

--

Method:
- since they are all digits, we know that d<=9, c<=8, b<=7, a<=6
    - this means that there are 126 different combinations of {a, b, c, d} to test
- there are 4 numbers available in {a, b, c, d}
    - they can be placed in 4 different locations
    - this gives us 4! possibilities = 24
- there are 4 operators available for any of 3 locations:
    - val = a (op1) b (op2) c (op3) d
    - this means we have 4x4x4 = 64 options per location
- the ways to use parentheses becomes more interesting
    - you can think of squishing the operations
    - using * as a generic operator:
        a * b * c * d
            ((a * b) * c) * d
            (a * b) * (c * d)
            (a * (b * c)) * d
            a * ((b * c) * d)
            (a * b) * (c * d)
            a * (b * (c * d))
- brute force

"""

import time
from fractions import Fraction
from itertools import permutations, product


t = time.time()


def evaluate_expression(numbers, operators, parentheses):
    # will take in iterables for 
    #   numbers, 
    #   operations, and 
    #   parenthesis locations (around which index operator)
    # returns the value of that expression

    # create list copies of inputs
    num_list = [f"Fraction({str(x)})" for x in list(numbers)]
    ops_list = list(operators)
    par_list = list(parentheses)

    # prep par list for shorten version of future num_list
    if par_list[1] > 0:
        par_list[1] -= 1

    # generate the parentheses portions of the expression
    for par in par_list:
        temp = "("

        temp += num_list[par]
        num_list.pop(par)
        
        temp += operators[par]
        ops_list.pop(par)
        
        temp += num_list[par]
        num_list.pop(par)

        temp += ")"
        
        num_list.insert(par, temp)
        
    # complete the expression
    try:
        expression = num_list[0] + ops_list[0] + num_list[1]
        return eval(expression)
    except ZeroDivisionError as e:
        return float('inf')


# generate all combinations for a, b, c, d
digit_combos = []
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                digit_combos.append([a, b, c, d])

# generate all permutations for a given set of operators
operators = ["*", "/", "+", "-"]
ops = list(product(operators, repeat=3))

# generate all permutations for parentheses
parentheses_locations = list(permutations(range(3), 2))

longest_chain = []
longest_chain_length = 0
for digit_combo in digit_combos:
    # generate all permutations for a given {a, b, c, d}
    num_perms = list(permutations(digit_combo))

    possible_values = set()
    # cycle through all permutations of numbers, 
    for num_perm in num_perms:
        for op in ops:
            for parentheses_location in parentheses_locations:
                # calculate the result and only add if it is greater than 0 and an integer
                res = float(evaluate_expression(num_perm, op, parentheses_location))
                if res > 0 and res.is_integer():
                    possible_values.add(int(res))

    # determine the length of consecutive integers starting at 1
    counter = 0
    while (counter + 1) in possible_values:
        counter += 1

    # compare to longest current length, save if higher
    if counter > longest_chain_length:
        longest_chain_length = counter
        longest_chain = digit_combo
        

print(f"{longest_chain=}")
print(f"{longest_chain_length=}")
print(f"{time.time() - t} sec")
