"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + (1 / (2 + 1/(2 + ...)))

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/77, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example
where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

---
Method:
- in iteration i, let the numerator be n and the denominator be d for ratio r:
             n
    r(i) =  ---
             d
- it can be observed that for i+1, the following are true:
                n + 2*d
    r(i+1) = -------------
                 d + n

- simply calculate the fraction for all values of i between 1 (r(1) == 3/2) and r(1000)
"""

ratios = [None] * 1000
ratios[0] = [3, 2]

for i in range(1, len(ratios)):
    n = ratios[i-1][0]
    d = ratios[i-1][1]
    ratios[i] = [n + 2*d, d + n]

res = [str(x[0]) < str(x[1]) for x in ratios]
ans = len([x for x in res if x])
print(f"ans == {ans}")

