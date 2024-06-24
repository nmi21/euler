from itertools import product

a_min = 2
a_max = 100
a = range(a_min, a_max + 1)

b_min = 2
b_max = 100
b = range(b_min, b_max + 1)


def int_comb(a, b):
    powers_list = []
    for x, y in product(a, b):
        powers_list.append(pow(x, y))
    return powers_list


def format_list(powers_list):
    return sorted(set(powers_list))


combined = int_comb(a, b)
ans = format_list(combined)

# print(combined)
# print(ans)
print(f"len == {len(ans)}")

