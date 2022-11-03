"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has
been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

---

Method:
- write a function that splits the digits, squares them, and then adds them
- implement memoization in order to decrease search

"""

LIMIT = 10000000

memo_dict = {
    1: 1,
    89: 89
}


def split_and_square(num):
    # if num % 100000 == 0:
    #     print(f"Checking {num}...")

    res = num
    while res != 1 or res != 89:
        if res in memo_dict:
            res = memo_dict[res]
            break
        s = 0
        for digit in str(res):
            s += int(digit) ** 2
        res = s

    memo_dict[num] = res

    return res


num_chain_res = [split_and_square(x) for x in range(1, LIMIT + 1)]
num_chain_89 = [ind for ind, ele in enumerate(num_chain_res) if ele == 89]
tot_89 = len(num_chain_89)

ans = tot_89
print(f"ans == {ans}")
