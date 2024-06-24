"""
This problem includes pictures. Thus, please refer to: https://projecteuler.net/problem=68

---
Method:
- we will always have more unknowns that we can have equations, and so one must try a few different initial inputs
and then we can determine the rest via linear algebra
- in the 3 gon case, we can make 4 equations, and therefore solve 4 unknowns
- in the 5 gon case, we have 10 total numbers and can form 6 total equations
- if we let [a, b, c, d, e] be the values for the outside numbers starting from the top and then going clockwise
    and we let [r, s, t, u, v] be the values for the inside numbers starting from the top and moving clockwise
    and we let z be the desired sum
    and we let y be the sum of all available numbers
    we can generate the following matrices in Ax = B form

    _                                          _   _       _     _     _
   |    1   0   0   0   0   1   1   0   0   0   | |     a   |   |   z   |
   |    0   1   0   0   0   0   1   1   0   0   | |     b   |   |   z   |
   |    0   0   1   0   0   0   0   1   1   0   | |     c   | = |   z   |
   |    0   0   0   1   0   0   0   0   1   1   | |     d   |   |   z   |
   |    0   0   0   0   1   1   0   0   0   1   | |     e   |   |   z   |
   |_   1   1   1   1   1   1   1   1   1   1  _| |     r   |   |_  y  _|
                                                  |     s   |
                                                  |     t   |
                                                  |     u   |
                                                  |_    v  _|

- since we are short 4 equations, we will need to search over the range of 4 different variables
    - if we set values for a, b, c, and d, we can remove those variables from the x vector and the associated columns
    that would otherwise be required
    - thus, we can get the following matrices in Ax = B form:

    _                          _   _       _     _                     _
   |    0   1   1   0   0   0   | |     e   |   |   z - a               |
   |    0   0   1   1   0   0   | |     r   |   |   z - b               |
   |    0   0   0   1   1   0   | |     s   | = |   z - c               |
   |    0   0   0   0   1   1   | |     t   |   |   z - d               |
   |    1   1   0   0   0   1   | |     u   |   |   z                   |
   |_   1   1   1   1   1   1  _| |_    v  _|   |_  y - a - b - c - d  _|

    - Then, using numpy's linear algebra tools, we can easily solve this system of linear equations

- from there, we will need to remove duplicate (rotated) solutions, and only using the smallest of those solutions
"""

import itertools
import numpy as np




"""
# # brute force solution for 3 gon ring
#
# n = 6
# nums = range(1, n+1)
# solutions = []
# for target in range(9, 13):
#     for a, b, c, r, s, t in itertools.product(nums, repeat=n):
#
#         # verify that each value is unique between 1 and n, else next iteration
#         letter_list = [a, b, c, r, s, t]
#         if set(nums) != set(letter_list):
#             continue
#
#         # verify that we have not already seen this solution but just rotated
#         not_unique = False
#         num_set = [a, r, s, b, s, t, c, t, r]
#         for sol in solutions:
#             first = num_set[:3]
#             if first == sol[:3] or first == sol[3:6] or first == sol[6:]:
#                 not_unique = True
#                 break
#
#         # if the solution is not unique, next iteration
#         if not_unique:
#             continue
#
#         # check the sums
#         check1 = a + r + s == target
#         check2 = b + s + t == target
#         check3 = c + t + r == target
#         check_sum = a + b + c + r + s + t == sum(list(nums))
#
#         if check1 and check2 and check3 and check_sum:
#             solutions.append([a, r, s, b, s, t, c, t, r])
#
#
# print(solutions)
# print(len(solutions))
"""


# # linear algebra solution for 3 gon
# for z in range(9, 13):
#     print(f"target == {z}")
#     for a, b in itertools.product(range(1, 7), repeat=2):
#
#         if a == b:
#             continue
#
#         coeffs = np.array([
#             [0, 1, 1, 0],
#             [0, 0, 1, 1],
#             [1, 1, 0, 1],
#             [1, 1, 1, 1]
#         ])
#
#         target = np.array([
#             z - a,
#             z - b,
#             z,
#             sum(range(1, 7)) - a - b
#         ])
#
#         res = list(np.linalg.solve(coeffs, target))
#         check = [int(x) for x in res if x == int(x)]
#         if len(check) != len(res):
#             continue
#
#         c, r, s, t = check
#         num_set = [a, r, s, b, s, t, c, t, r]
#         if set(num_set) != set(range(1, 7)):
#             continue
#
#         print(num_set)

# linear algebra solution for 5gon

n = 10
nums = range(1, n+1)
min_sum = 1 + 2 + 3
max_sum = 10 + 9 + 8
possible_sums = list(range(min_sum, max_sum+1))
solutions = {}
for z in possible_sums:
    solutions[z] = []
    for a, b, c, d in itertools.product(nums, repeat=4):

        changing_vals = [a, b, c, d]
        if len(set(changing_vals)) < len(changing_vals):
            continue

        coeffs = np.array([
            [0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
        ])

        target = np.array([
            z - a,
            z - b,
            z - c,
            z - d,
            z,
            sum(nums) - a - b - c - d
        ])

        res = list(np.linalg.solve(coeffs, target))
        check = [int(x) for x in res if x == int(x)]
        if len(check) != len(res):
            continue

        e, r, s, t, u, v = check
        ring_set = [[a, r, s], [b, s, t], [c, t, u], [d, u, v], [e, v, r]]
        flat_list = list(itertools.chain(*ring_set))
        if set(flat_list) != set(nums):
            continue

        """
        Since the search tree starts with the lowest values of a, we can reject other sets that are present that contain
        [a, r, s] as any one of the other ring elements 
        """
        unique = True
        for sol in solutions[z]:
            first_nums = sol[0]
            if first_nums in ring_set:
                unique = False
                break
        if not unique:
            continue

        solutions[z].append(ring_set)

# remove empty solutions
solutions = {key: val for (key, val) in solutions.items() if val}

# remove keys and flatten to a list
solutions_list = [x for x in solutions.values()]
solutions_list = [list(itertools.chain(*x)) for sublist in solutions_list for x in sublist]

# form strings from each element in each solution
string_solutions = [''.join(map(str, x)) for x in solutions_list]

# get only the 16 digit strings and convert to ints
res = [int(x) for x in string_solutions if len(x) == 16]

ans = max(res)
print(f"ans == {ans}")
