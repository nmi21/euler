


def num_digits(num):
    return len(str(num))


num = 2
n_1 = 1
n_2 = 1
n = 3

stop = 1000

while num_digits(num) < stop:
    n_2 = n_1
    n_1 = num
    num = n_1 + n_2
    n += 1

print(f"fn == {num}")
print(f"n == {n}")