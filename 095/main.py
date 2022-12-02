"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of
28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a
chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""
num_limit = 1000000


def factors_sieve(limit):

    sieve = [1] * limit
    sieve[0] = 0

    for i in range(2, limit):
        for j in range(2*i, limit, i):
            sieve[j] += i

    return sieve


def build_chain(n, factor_sum_sieve):

    chain = [n]

    while True:
        next_num = factor_sum_sieve[chain[-1]]
        if next_num == n:
            break
        if (next_num in chain) or (next_num >= num_limit) or (next_num == 1):
            return []
        chain.append(next_num)

    return chain


factor_sums = factors_sieve(num_limit + 1)
max_length = 0
max_chain = []
for i in range(2, num_limit + 1):
    chain = build_chain(i, factor_sums)
    if len(chain) > max_length:
        max_length = len(chain)
        max_chain = chain

ans = min(max_chain)
print(f"ans == {ans}")

