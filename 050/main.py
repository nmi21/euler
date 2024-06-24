def sieve_of_eratosthenes(limit):
    sieve = [True for i in range(limit + 1)]
    sieve[0] = False
    sieve[1] = False
    n = 2
    while n <= limit:
        if sieve[n]:
            for i in range(n+n, limit + 1, n):
                sieve[i] = False
        n += 1
    primes = []
    for ind, ele in enumerate(sieve):
        if ele:
            primes.append(ind)
    return primes


limit = 1000000
primes = sieve_of_eratosthenes(limit)

# TODO create a max length solver
max_sum = 0
max_run = 0
for i in range(len(primes)):
    s = 0
    counter = 0
    for j in range(i, len(primes)):
        counter += 1
        s += primes[j]
        if s > limit:
            break
        if (s in primes) and (counter > max_run):
            max_sum = s
            max_run = counter
            print(f"max_sum == {max_sum}")
            print(f"max_run == {max_run}")
            print()

print(f"max_sum == {max_sum}")
print(f"max_run == {max_run}")
