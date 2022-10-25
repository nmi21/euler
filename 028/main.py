"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
Assumptions:
- the n x n grid only works on cases where n % 2 == 1
- in all cases where n > 1, the numbers can be calculated in the following way:
    - top right    = n ** 2
    - top left     = n ** 2 -   (n-1)
    - bottom left  = n ** 2 - 2*(n-1)
    - bottom right = n ** 2 - 3*(n-1)
- Combined, the value for any outer values (where n > 1) can be calculated by adding those together"
    - 4*(n ** 2) - 6*n + 6
- Thus, we can add all sums of sprials in n from 1 to 1001
"""

def spiral_solver(n):
    if n % 2 == 0:
        return "needs to be odd"
    if n == 1:
        return 1
    return 4*(n ** 2) - 6*n + 6


ans = 0
for n in range(1, 1001+1, 2):
    ans += spiral_solver(n)

print(f"ans == {ans}")