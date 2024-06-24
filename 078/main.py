"""
Let p(n) represent the number of different ways in which n coins can be separated into piles.

For example, five coins can be separated into piles in exactly seven different ways, so p(5) = 7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

--
Method:
https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Examples

https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Generating_function

- Use the generator function to generate all of the possible pentagonal values needed
- continue to add to a list for partition numbers
- use % 1,000,000 to keep numbers reasonable (and also for a verification check!)
- when the last number added % 1,000,000 == 0, abort search
- the index of the last number (length of list - 1) will be the first term that satisfies the condition
"""

import time
t = time.time()


def pentagonal(k):
    return k*(3*k - 1) // 2


# generate all of the k values we might need
k_list = []
for i in range(1, 1_000_000 + 1):
    k_list.append(i)
    k_list.append(-i)

# generate all of the associated pentagonal numbers we might need
pent_list = []
for k in k_list:
    pent_list.append(pentagonal(k))

mod = 1_000_000
part_list = [1]  # only 1 way to partition 0
while part_list[-1] % mod != 0:
    next_part = 0
    for i in range(len(pent_list)):
        if pent_list[i] > len(part_list):
            break
        sign = 1
        if i % 4 >= 2:
            sign *= -1
        next_part += sign * part_list[-pent_list[i]]
    part_list.append(next_part % mod)

ans = len(part_list) - 1
print(f"{ans=}")

print(f"{time.time() - t} sec")
