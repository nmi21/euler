"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

---
Method:
- implement recursion over all numbers just shy of the target
- the purely recursive method is too slow, and thus may need to implement memoization

"""

import time
t = time.time()


TARGET = 100
POS_INTS = list(range(1, TARGET - 1))


def find_sum_ways(num_sum, limit, nums_available, current_num_pointer):

    num_ways = 0

    if current_num_pointer >= len(nums_available):
        return num_ways

    while num_sum < limit:
        num_ways += find_sum_ways(num_sum, limit, nums_available, current_num_pointer + 1)
        # print(f"{'_' * current_num_pointer} Adding {nums_available[current_num_pointer]}...")
        num_sum += nums_available[current_num_pointer]
        # print(f"num_sum == {num_sum}")

    if num_sum == limit:
        # print("Solution found!")
        num_ways += 1

    return num_ways


def solve():
    start_sum = 0
    start_pointer = 0

    return find_sum_ways(num_sum=start_sum, limit=TARGET, nums_available=POS_INTS, current_num_pointer=start_pointer)


ans = solve()
print(ans)

"""
The above method took 361 seconds to complete when looking for the total number of ways to sum to 100. 
Thus, we will need a different, faster algorithm. 
"""







print(f"{time.time() - t} sec")
