"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?

"""

from itertools import product


def is_pandigital(num):
    num = str(num)
    if len(num) != 9:
        return False
    pan_str = "123456789"
    for digit in pan_str:
        if digit not in num:
            return False
    return True


pan_prods = []
# only need to check up to 10000 because "10000" + "20000" = "1000020000"
# and is > 987654321 and satisfies n > 1
lim = 10000
for x in range(1, lim + 1):
    # print(f"checking x == {x}...")
    concat_str = ""
    n = 1
    while len(concat_str) < 10:
        # print(f"adding {n*x}")
        concat_str += str(n * x)
        n += 1
        # print(concat_str)
        if is_pandigital(concat_str) and n > 1:
            pan_prods.append(int(concat_str))
            # print(pan_prods)

pan_prods.sort(reverse=True)
ans = pan_prods[0]

print(f"ans == {ans}")
