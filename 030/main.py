"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


# write a function to determine sum of each digit
def fifth_power_sum(num):
    num = str(num)
    total_sum = 0
    for digit in num:
        total_sum += int(digit) ** 5
    return total_sum


# write a function to check against value of input number
def check_fifth_power(num):
    return fifth_power_sum(num) == num


# determine max search value
x = 1
while ((9 ** 5) * x) > (10 ** x):
    x += 1

# print(x)
search_lim = 10 ** x

# if sum == num, add to a list
fifth_powers_nums = []
for num in range(10, search_lim+1):
    if check_fifth_power(num):
        fifth_powers_nums.append(num)

print(fifth_powers_nums)

# sum list
ans = sum(fifth_powers_nums)
print(f"ans == {ans}")
