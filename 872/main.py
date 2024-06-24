"""
https://projecteuler.net/problem=872

--

Method:
- The first thing to notice is how you can build a tree for T(n):
    - T(n) is even, the first branch will always be odd, and all other branches will be even
    - T(n) is odd, the first branch will always be even, and all other branches will be odd
- The difference between branch nodes are powers of 2, increasing both down and across

- For example, draw T(17):
    - 17
        - 16
            - 14
                - 10
                    - 2
                - 6
            - 12
                - 4
            - 8
        - 15
            - 11
                - 3
            - 7
        - 13
            - 5
        - 9
        - 1

You can find k in f(n, k) and build back up to the top
Then cascade back down to the bottom.
"""

import time
import math

t = time.time()

def f(n, k):
    
    # start with counter as value we are seeking
    counter = k
    
    # if the value is in the first brach, add the n value and just search within first brach
    if n - k % 2 == 1:
        counter += n
        n -= 1

    # build up from k to branch node
    temp = k
    while temp < n:
        exp = int(math.log2(n - temp))
        temp += 2**exp
        counter += temp
    
    # build down to bottom node
    exp = int(math.log2(n - k)) + 1
    temp = k
    while temp - 2**exp > 0:
        temp -= 2**exp
        counter += temp
        exp += 1

    return counter


n = 10 ** 17
k = 9 ** 17
ans = f(n, k)
print(f"{ans=}")

print(f"{time.time() - t} sec")
