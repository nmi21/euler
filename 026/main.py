"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

   [1/0 =   NaN             -1]
   [1/1 =   1               -1]
    1/2	= 	0.5             0
    1/3	= 	0.(3)           1
    1/4	= 	0.25            0
    1/5	= 	0.2             0
    1/6	= 	0.1(6)          1
    1/7	= 	0.(142857)      6
    1/8	= 	0.125           0
    1/9	= 	0.(1)           1
    1/10	= 	0.1         0

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

------

Method:
- using old school style division:
    - divide 1 by num, find the remainder
    - multiply by 10 subtract out what you can, find the remainder, etc

"""


def find_cycle(denom):
    # print("---------------------------")
    # print(f"denom == {denom}")
    # print("---------------------------")

    # define -1 to be a nonsensical answer e.g. 1/0
    if denom < 2:
        return -1
    qr = (0, 1)  # quotient remainder pair
    divs = []
    while qr not in divs:
        divs.append(qr)
        num = divs[-1][1] * 10  # remainder of last qr pair
        qr = (num // denom, num % denom)
        # print(f"qr == {qr}")
    if qr == (0, 0):
        return 0
    return len(divs) - divs.index(qr)


lim = 1000
repeating_period = [find_cycle(x) for x in range(lim)]

max_period = max(repeating_period)
ans = repeating_period.index(max_period)

print(f"max_period == {max_period}")
print(f"ans == {ans}")

