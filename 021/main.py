from math import *


def find_divisors(num):
    '''
    :param num: number to be checked
    :return: list of divisors for num
    '''
    stop = floor(num / 2)
    div_list = []
    for i in range(1, stop + 1):
        if num % i == 0:
            div_list.append(i)
    return div_list


def sum_divisors(num):
    return sum(find_divisors(num))


# TODO create amicable checker

def amicable_checker(num):
    a = num
    b = sum_divisors(a)
    if a == b:
        return False
    if a == sum_divisors(b):
        return True
    return False


amicables = []
start = 1
stop = 10000

for i in range(start, stop + 1):
    if amicable_checker(i):
        amicables.append(i)

ans = sum(amicables)
print(amicables)
print(ans)
