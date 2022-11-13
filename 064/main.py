"""
Description:
https://projecteuler.net/problem=64

---
Method:
- a0 is relatively easy to calculate:
    - it is the square root the nearest perfect square less than the sqrt being calculated
        - e.g. if we are calculating sqrt(N), then a0 = int(sqrt(N))
- this lays out a method to determine the values for ai:
    https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html#section6
    - this points out that a cycle will always end when ai == 2*a0 for reasons I don't understand
- thus, stop the loop when ai = 2*a0
- the period length will simply be the length of the tuple

"""
import math


def contfract(N):

    if int(math.sqrt(N)) ** 2 == N:
        return [int(math.sqrt(N)), ()]

    N_list = [math.sqrt(N), 1]
    a_list = [int(N_list[0] / N_list[1])]
    while a_list[-1] != 2 * a_list[0]:
        next_N = N_list[-2] % N_list[-1]
        N_list.append(next_N)
        a = int(N_list[-2] / N_list[-1])
        a_list.append(a)

    return [a_list[0], tuple(a_list[1:])]


def contfract_period_length(N):
    return len(contfract(N)[1])


limit = 13
period_lengths = [contfract_period_length(x) for x in range(1, limit+1)]
odd_periods = [ind + 1 for ind, ele in enumerate(period_lengths) if ele % 2 == 1]
print(len(odd_periods))


