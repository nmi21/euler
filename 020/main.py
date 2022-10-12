from math import *


def digits_add(num):
    fac = factorial(num)
    digit_list = [int(x) for x in [*str(fac)]]
    return sum(digit_list)


num = 100
print(digits_add(num))
