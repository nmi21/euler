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

---
How to solve continued fractions:
- If we take the general example as seen in Knott's section 6.2.2, we can see that a pattern emerges:
    - we first subtract the integer portion of sqrt(N) from N and then we are left with a ratio that is added to sqrt(N)
    - we know that this ratio must be < 1, because (int(sqrt(N)) + 1)^2 > N
    - as we continue to evaluate values of x, the denominator is always of the form "sqrt(N) - m"
        - we can show this from the previously noted ratio 1 / xi must be less than 1 in all cases
    - we can evaluate x1 to be
        numerator: sqrt(N) + int(sqrt(N))
        denominator: N - int(sqrt(N))**2
    - then a1 is just int(x1)
"""
import math


def contfract(N):

    if int(math.sqrt(N)) ** 2 == N:
        return [int(math.sqrt(N)), ()]

    """
    fraction of the form x_i = r / (sqrt(N) - p)
    transforms into (sqrt(N) + p) / ((N - p**2)/r)
    
    we can redefine r to be the denominator of the previous: r = (N - p**2)/r
    we can then extract the integer portion and call that a_i
    then we can rewrite the equation as 
        x_i = a_i + (sqrt(N) + (p - a_i*r))/r
    we can redefine p as
        p = p - a_i*r
        
    then we know that x_(i+1) can be written as r / (sqrt(N) - p) and continue to calculate!
    """

    a_list = [int(math.sqrt(N))]
    r = 1
    p = a_list[0]

    while a_list[-1] != 2*a_list[0]:
        # print(f"x_i == {r} / (sqrt({N}) - {p})")
        r = int((N - p**2) / r)
        # print(f"x_i == (sqrt({N}) + {p}) / {r}")
        a_i = int((math.sqrt(N) + p) / r)
        p = abs(p - a_i*r)
        a_list.append(a_i)

    return [a_list[0], tuple(a_list[1:])]


def contfract_period_length(N):
    return len(contfract(N)[1])


limit = 10000
period_lengths = [contfract_period_length(x) for x in range(1, limit+1)]
odd_periods = [ind + 1 for ind, ele in enumerate(period_lengths) if ele % 2 == 1]

ans = len(odd_periods)
print(f"ans == {ans}")
