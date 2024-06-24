"""
https://projecteuler.net/problem=493

70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal pint (a.bcdefghij).

--

Method:

Monte Carlo simulation is going to take too long to be sufficiently precise.

Looking back at the wording of the problem, we are looking to find the distinct number of colors selected.

So what is the probability that any one of the seven colors (ROYGBIV) is selected?

The chance that any one color is selected is the same as

    1 - P(not selected)


To get the probability that any one color gets selected, let's start by seeing what 
the chance that that particular color does not get selected.

There are
    (70 choose 20)=161884603662657876
ways to select 20 balls total from a set of 70.

How many of them don't select a ball of a certain color? There are
    (60 choose 20)=4191844505805495
ways to get 20 balls from 60 (that is: 70 total to choose from but only selected 
from the 60 that are not of desired color).

So there is a
    (60 choose 20) / (70 choose 20)≈2.589%
chance of not getting that specific color.

Expanding, we can see that there is a
    1 - (60 choose 20) / (70 choose 20) ≈ 97.411% 
chance of getting the specific color!

Alternatively stated: each color has a 0.97411 expected value of appearing.

We simply need to multiply this by the total number of colors! (and then 
round to the correct number of digits).

"""

import time

t0 = time.time()


def choose(n, k):
    greater = k
    lesser = n - k

    if lesser > greater:
        greater = n - k
        lesser = k

    prod = 1

    start = greater + 1
    for i in range(start, n + 1):
        prod *= i
    
    for i in range(1, lesser + 1):
        prod = prod // i

    return prod


def solve(num_colors=7,
    num_per_color=10, 
    num_balls_picked=20, 
    digits_after_decimal=9):

    total_balls = num_colors * num_per_color
    excluded = total_balls - num_per_color

    ans = num_colors * (1 - choose(excluded, num_balls_picked) / choose(total_balls, num_balls_picked))

    # round the answer to correct digits
    ans = round(ans, digits_after_decimal)

    return ans


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t0} sec")
