"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

from nums_sequence import nums

nums = nums.splitlines()
# print(nums)

total = 0
for line in nums:
    total +=  int(line)

ans = str(total)[0:10]
print(f"ans == {ans}")
