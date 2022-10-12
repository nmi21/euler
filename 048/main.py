start = 1
stop = 1000
num_digits = 10

def self_powers(start, stop):
    total = 0
    for x in range(start, stop + 1):
        total += pow(x, x)
    return total


val = self_powers(start, stop)
# print(val)
digits = str(val)[-num_digits:]
print(digits)
