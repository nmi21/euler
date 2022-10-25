"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Method:
- we know that we only care about the first 1,000,000 characters
- we can determine how many digits each "range" uses:
- we only need to go until the total characters reaches 1,000,000, which is < num == 1,000,000

min       max       digits  *   numbers =   total
---       ---       ------      ------- =   -----
1         9         1       *   9       =   9
10        99        2       *   90      =   180
100       999       3       *   900     =   2,700
1,000     9,999     4       *   9,000   =   36,000
10,000    99,999    5       *   90,000  =   450,000
100,000   999,999   6       *   900,000 =   5,400,000

# def d_num(n):
#     deltas = [9, 180, 2700, 36000, 450000, 5400000]
#     if n < 1:
#         return None
#     # first find the number that it belongs to by finding the "bin" it fits in
#     elif n < 10:
#         return n
#     elif n < 100:
#         start = 10
#         delta = sum(deltas[:2])
#     elif n < 1000:
#         start = 100
#         delta = sum(deltas[:3])
#     elif n < 10000:
#         start = 1000
#         delta =
#     elif n < 100000:



On second thought.... python can deal with strings quite easily
- generate the string
- grab the value from each d(n) listed
- multiple them together
"""

from math import prod

n = 1
d_str = "0"
while len(d_str) < 1000001:
    d_str += str(n)
    n += 1

n = 1
d = []
while n < 1000001:
    d.append(int(d_str[n]))
    n *= 10

ans = prod(d)
print(f"ans == {ans}")