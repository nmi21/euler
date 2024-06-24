"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""


def is_permutable(num):
    num = str(num)
    for mult in range(2, 7):
        perm = str(mult * int(num))
        # print(f"num == {num}")
        # print(f"perm == {perm}")
        if len(perm) != len(num) or set(perm) != set(num):
            return False
    return True


x = 1
while not is_permutable(x):
    x += 1

ans = x
print(f"ans == {x}")
