import time
import math

t = time.time()


def sieve_of_eratosthenes(lim):
    # use a sieve to determine primes

    sieve = [True] * (lim + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(4, lim + 1, 2):
        sieve[i] = False
        
    for i in range(3, lim + 1, 2):
        if sieve[i]:
            for j in range(3 * i, lim + 1, 2 * i):
                sieve[j] = False
                
    return sieve


def get_primes(lim):
    # pull the actual values for primes from sieve
    return [ind for ind, ele in enumerate(sieve_of_eratosthenes(lim)) if ele]


def get_max_q(r, s=1):
    # obtain max value for q to satisfy equation  

    log_2_r = math.log2(r)
    
    q = 2

    while 2*q + 2*math.log2(2*q) <= s*log_2_r:
        q *= 2
    
    
    while (q+1) + 2*math.log2(q+1) <= s * log_2_r:
        q += 1
    
    return q


def solve(r=800800, s=800800):

    s_log2_r = s * math.log2(r)
    primes = get_primes(get_max_q(r, s))
    primes_log2 = [math.log2(x) for x in primes]

    def check_hybrids(p_ind, q_ind):
        # evaluate expression using indices
        return primes[q_ind]*primes_log2[p_ind] + primes[p_ind]*primes_log2[q_ind] <= s_log2_r

    # get max prime index to check
    last_p = None
    for p in range(len(primes)):
        if not primes[p+1]*primes_log2[p] + primes[p]*primes_log2[p+1] <= s_log2_r:
            # we have reached the end of possibilities
            last_p = p
            break

    # count to get result
    count = 0
    last_q = len(primes) - 1
    for p in range(last_p):
        for q in range(last_q, p, -1):
            if check_hybrids(p, q):
                count += q - p
                last_q = q
                break

    return count


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t} sec")
