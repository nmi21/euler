"""
Sum         Num ways        Way1        Way2        Way3        Way4        Way5        Way6
2           1               1+1
3           2               1+1+1       1+2
4           4               1+1+1+1     1+1+2       2+2         1+3
5           6               1+1+1+1+1   1+1+1+2     1+1+3       1+2+2       2+3         1+4

"""


import time
t = time.time()

# set the end target (the number we will count up to)
TARGET = 100

# create an array called "ways" representing the number of ways that index, i, can be summed using positive integers
ways = [0] * (TARGET + 1)
ways[0] = 1     # set 0 to 1 because you can only reach it 1 way --> not having anything

for i in range(1, TARGET):              # iterate over the positive integers
    for j in range(i, TARGET + 1):      # iterate over all the indices of ways
        ways[j] += ways[j - i]

# print(ways)
ans = ways[-1]
print(f"ans == {ans}")

print(f"{time.time() - t} sec")