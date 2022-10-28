"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

---

Method:
- largest composite number from 2 3-digit numbers is 999*999
- smallest is 100*100
- search space is small enough that can search over entire space
"""


def is_palindrome(x):
    x = str(x)
    return x == x[::-1]


palins = []
for x in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(x*y):
            palins.append(x*y)

# print(palins)
# print(len(palins))
ans = max(palins)
print(f"ans == {ans}")
