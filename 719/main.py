"""
We define an S-number to be a natural number, n, that is a perfect square and its square root
can be obtained by splitted the decimal representation of n into 2 or more numbers then adding 
the numbers.

For example, 81 is an S-number be sqrt(81) = 8 + 1
6724 is an S-number: sqrt(6724) = 6 + 72 + 4
8281 is an S-number: sqrt(8281) = 8 + 2 + 81 = 82 + 8 + 1
9801 is an S-number: sqrt(9801) = 98 + 0 + 1

Further we define T(N) to be the sum of all S numbers n <= N. You are given T(10^4) = 41333.

Find T(10^12).

-- 

Method:
- Generate a perfect square
- split the perfect square into all possible strings
- sum each of the ways to see if you return a valid summation
"""

import time
import math

t = time.time()


def splitter(s):
    # yields all ways to split a string
    for i in range(1, len(s)):
        start = s[0:i]
        end = s[i:]
        yield [start, end]
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result


def check_split_sum(n):
    # return bool
    # if a string split of n**2 can be summed to n, return True
    combos = list(splitter(str(n**2)))
    sums = [sum([int(x) for x in y]) for y in combos]

    for s in sums:
        if s == n:
            return True

    return False


limit = 10 ** 12
poss = [x for x in range(1, int(math.sqrt(limit) + 1)) if x % 9 == 0 or x % 9 == 1]

s_nums = []
for p in poss:
    if check_split_sum(p):
        s_nums.append(p**2)

print(f"{limit=}")
print(f"{sum(s_nums)}")
print(f"{len(s_nums)=}")


# print(f"{ans=}")

print(f"{time.time() - t} sec")


"""
limit=10000
len(s_nums)=9
0.0004303455352783203 sec

limit=100000
len(s_nums)=11
0.0013339519500732422 sec

limit=1000000
len(s_nums)=28
0.008971691131591797 sec

limit=10000000
len(s_nums)=33
0.08283066749572754 sec

limit=100000000
len(s_nums)=75
0.3437826633453369 sec

limit=1000000000
len(s_nums)=84
2.3383939266204834 sec

limit=10000000000
len(s_nums)=165
13.842710971832275 sec

limit=100000000000
len(s_nums)=189
118.58763360977173 sec
"""
