"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

"""
-- there are 10 total digits, therefore there are 10! == 3,628,800 possible permutations
-- we know that the first digit contains 9! == 362880 possible combinations
-- therefore we know that 1,000,000 / 9! ~= 2.75
-- otherwise stated we haven't made it thru the 3rd digit yet, and so we would expect the first digit to be 2
-- we should be able to find the 274240th combination of 0 - 9 without 2
"""


from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def lexicographic(num_list):
    perms = list(permutations(num_list, len(num_list)))
    ans = []
    for perm in perms:
        num = ""
        for dig in perm:
            num += str(dig)
        ans.append(num)
    return ans


ind = 1000000
ind -= 1
lex = lexicographic(digits)
ans = lex[ind]
print(ans)
