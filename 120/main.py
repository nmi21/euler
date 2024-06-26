"""
Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.

--
Method:

"""

def p120(a, n):
    return ((a-1)**n + (a+1)**n) % a**2

for i in range(3, 1001):
    for n in range(0, i):
