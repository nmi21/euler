def sieve_of_eratosthenes(num):
    """
    Efficient algorithm to calculate all prime numbers below a max_num

    :param num: maximum number to be calculated to, not inclusive
    :return: a list of all primes below max_num
    """
    sieve = [True for i in range(num)]
    sieve[0] = sieve[1] = False
    i = 2
    while i * i < num:
        if sieve[i]:
            for j in range(i * i, num, i):
                sieve[j] = False
        i += 1
    primes = [x for x in range(num) if sieve[x]]
    return primes


def truncate_left_to_right(num):
    return int(str(num)[1:])


def truncate_right_to_left(num):
    return int(str(num)[:-1])


def truncated_list(num):
    out = [num]
    iters = len(str(num)) - 1

    left = num
    for _ in range(iters):
        left = truncate_left_to_right(left)
        out.append(left)

    right = num
    for _ in range(iters):
        right = truncate_right_to_left(right)
        out.append(right)

    return out


def possibly_truncatable(num):
    if num <= 7:
        return False
    s = str(num)
    evens = [str(digit) for digit in [0, 2, 4, 6, 8]]
    if any(digit in evens for digit in s[1:]):
        return False
    if any("5" == digit for digit in s[1:]):
        return False
    return True


limit = 100


truncatable = []
while len(truncatable) < 11:
    print(f"checking against limit == {limit}...")
    truncatable = []
    primes = sieve_of_eratosthenes(limit)
    for prime in primes:
        if possibly_truncatable(prime):
            if all(n in primes for n in truncated_list(prime)):
                truncatable.append(prime)
    print(f"total truncatable primes == {len(truncatable)}")
    limit *= 10

print()
print(f"truncatable == {truncatable}")
print()

ans = sum(truncatable)
print(f"ans == {ans}")