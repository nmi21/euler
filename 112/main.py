"""
https://projecteuler.net/problem=112
-- 
Method:
- check if a number is bouncy by checking if it is neither
    - increasing
    - decreasing
- note: repunits seem to classify as both increasing and decreasing
- stick to integer math to make calculations faster (rather than
casting numbers to strings)
"""

import time

t0 = time.time()


def is_decreasing(num):
    
    temp = num
    
    prev = temp % 10
    temp //= 10
    while temp > 0:
        current = temp % 10
        
        if current < prev:
            return False
        
        prev = current
        temp //= 10
        
    return True


def is_increasing(num):
    
    temp = num
    
    prev = temp % 10
    temp //= 10
    while temp > 0:
        current = temp % 10
        
        if current > prev:
            return False
        
        prev = current
        temp //= 10
        
    return True


def is_bouncy(num):
    return not is_decreasing(num) and not is_increasing(num)


def solve(target):
    """
    Solves number at which bouncy numbers reach exactly a target ratio.
    That ratio is bouncy / total numbers.

    Numbers start at 1.

    target should be between [0, 1]
    """

    bouncy = 0
    total = 0

    i = 1
    while True:
        
        total += 1

        if is_bouncy(i):
            bouncy += 1

        if bouncy / total == target:
            return total
        
        i += 1


target = .99
ans = solve(target)

print(f"{ans=}")
print(f"{time.time() - t0} sec")
