"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
2^6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been
found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.

"""

exp = 7830457
# exp = 3


def last_10(num):
    return int(str(num)[-10:])


res = 2
for i in range(1, exp):
    res *= 2
    res = last_10(res)

res = last_10(28433 * res + 1)

ans = res
print(f"ans == {ans}")
