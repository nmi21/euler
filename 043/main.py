"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

---

Method:
- there are only 9 * 9! answers possible, so it is probably easiest to just brute force
- (the reason it isn't 10! is because can't start with 0)
"""

from itertools import permutations


def check_mods(num):
    """
    take in a num (either str or int) and then determine if it fits the mod rules as laid out in problem description
    :param num:
    :return: Bool
        True if acceptable
        False if not
    """
    num = str(num)
    mod_nums = [2, 3, 5, 7, 11, 13, 17]
    for ind in range(1, 8):
        check_num = int(num[ind: ind + 3])
        if check_num % mod_nums[ind - 1] != 0:
            return False
    return True


pan_nums = "0123456789"
perms = [''.join(tup) for tup in list(permutations(pan_nums)) if tup[0] != '0']

divisible = [int(num) for num in perms if check_mods(num)]
print(divisible)

ans = sum(divisible)
print(f"ans == {ans}")

