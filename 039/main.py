"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

- we know that p = a + b + c
- we also know that, since it is a right triangle, a^2 + b^2 = c^2

Strategy
- iterate from p = 1 to p = 1000
- start with a = 1, b = 1
- calculate c = p - a - b
- determine if right triangle via pythagorean theorem
- if yes, add to counter
- if no, next iteration
"""

import itertools

limit_p = 1000
p_max_sol = None
sols_max = 0
solutions = []
# iterate over p in range specified in problem
for p in range(1, limit_p + 1):
    # intitialize solutions at 0 for each value of p
    sols = 0
    sols_list = []
    for a in range(1, p):
        for b in range(1, a):
            c = p - a - b
            pythagorean_check = c ** 2 == a ** 2 + b ** 2
            # if the values are valid, add to total solutions
            if c > 0 and pythagorean_check:
                sols += 1
                sols_list.append([a, b, c])
    if sols > sols_max:
        sols_max = sols
        p_max_sol = p
        solutions = sols_list
        print(f"New max: p == {p}")
        print(f"num_sols == {len(solutions)}")
        print(f"solutions == {solutions}")
        print()

print(solutions)
ans = p_max_sol
print(f"ans == {ans}")
