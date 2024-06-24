import math


# create a factorial dictionary
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fact_dict = {str(x):math.factorial(x) for x in digits}

# TODO break up a number into each digit and find sum
def dig_sum(num):
    sum = 0
    for dig in str(num):
        sum += fact_dict[dig]
    if sum == num:
        return True
    return False

dig_facts = []
start = 3
stop = 1000000
for x in range(start, stop):
    if dig_sum(x):
        dig_facts.append(x)

ans = sum(dig_facts)
print(ans)