"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

----
Method:
- to avoid recalculating values, create a
"""

LIMIT = 999999
num_terms = [0] * (LIMIT + 1)
num_terms[1] = 1


def collatz(n):
    if n < LIMIT + 1 and num_terms[n]:
        return num_terms[n]

    count = 1
    while n > 1:
        # if we have already calculated this number, retrieve it
        if n < LIMIT + 1 and num_terms[n]:
            return count + num_terms[n]

        # handler for n depending on even/odd
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3*n + 1

        count += 1

    return count


# calculate Collatz sequence length for all values < 1000000
for i in range(1, LIMIT + 1):
    num_terms[i] = collatz(i)

ans = num_terms.index(max(num_terms))
print(f"ans == {ans}")
