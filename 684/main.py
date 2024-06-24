"""
https://projecteuler.net/problem=684

--

Method:
There is a bit of derivation involved:
- first we can see how to solve for s(n):
    - let q = n // 9, r = n % 9
    - s(n) = (r + 1) * 10**q - 1
- for S(k), we can write it out as a sum:
    - S(k) = sigma(n=1, k){s(n)}
    - S(k) = sigma(n=1, k){(r+1)*10**q - 1} for each q, r
        - can pop out the constant
    - S(k) = sigma(n=1, k){(r+1)*10**q} - sigma(n=1, k){1}
    - S(k) = sigma(n=1, k){(r+1)*10**q} - k
    - S(k) = -k + {10**0 * sigma(r=0, 8){r+1} - 1} + {10**1 * sigma(r=0, 8){r+1}} + ... 
        + {10**(q_k - 1) * sigma(r=0, 8){r+1}} + {10**0 * sigma(r=0, r_k){r+1}}
            pull out the constant, 1
    - S(k) = -k - 1 + {10**0 * sigma(r=0, 8){r+1}} + {10**1 * sigma(r=0, 8){r+1}} + ... 
        + {10**(q_k - 1) * sigma(r=0, 8){r+1}} + {10**0 * sigma(r=0, r_k){r+1}}
            - note that sigma(r=0, 8){r+1} = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
            - simplify
    - S(k) = -k - 1 + {10**0 * 45 + 10**1 * 45 + ... + 10**(q_k - 1) * 45} + {10**0 * sigma(r=0, r_k){r+1}}
            - factor out the 45
    - S(k) = -k - 1 + 45 * {10**0 + 10**1 + ... + 10**(q_k - 1)} + {10**0 * sigma(r=0, r_k){r+1}}
            - note that 10**0 + 10**1 + 10**2 + ... + 10**n is a repunit
            - repunit with n digits is (10**n - 1)/9
            - here we have from 0 to q_k - 1, so we will have q_k number of digits
            - subsitute repunit equation
    - S(k) = -k - 1 + 45*{(10**q_k - 1) / 9} + {10**q_k * sigma(r=0, r_k){r+1}}
            - simplify 45/9
    - S(k) = -k - 1 + 5*(10**q_k - 1) + {10**q_k * sigma(r=0, r_k){r+1}}
            - distribute the 5
    - S(k) = -k - 1 + 5*10**q_k - 5 + {10**q_k * sigma(r=0, r_k){r+1}}
            - simplify
    - S(k) = -k - 6 + 5*10**q_k + {10**q_k * sigma(r=0, r_k){r+1}}

We want the answer modulo 1_000_000_007, and so we can distribute a modulo operator
    - want S(k) % m
    - from modular math identities:
        - a*b % m == ((a%m) * (b%m)) % m
        - (a + b) % m == ((a % m) + (b % m)) % m
    - S(k) = ((-k - 6)%m + (5*10**q_k)%m + {10**q_k * sigma(r=0, r_k){r+1}}%m) % m

"""

import time

t = time.time()


def S(k, m=1_000_000_007):

    # S(k) = -k - 6 + 5*10**q_k + {10**q_k * sigma(r=0, r_k){r+1}}

    q_k = k // 9
    r_k = k % 9
    
    sub_sum1 = ((5 % m) * pow(10, q_k, m)) % m
    
    sub_sum2 = 0
    for r in range(r_k + 1):
        sub_sum2 += r + 1
    sub_sum2 = ((sub_sum2 % m) * pow(10, q_k, m)) % m
    
    sub_sum3 = ((k % m) + (6 % m)) % m
    
    S_k = ((sub_sum1 % m) + (sub_sum2 % m) - (sub_sum3 % m)) % m
    
    return S_k
    

def solve():

    m = 1_000_000_007

    # get the first 90 fibonacci numbers
    fibs = [0, 1]
    while len(fibs) <= 90:
        fibs.append(fibs[-1] + fibs[-2])
    
    res = 0
    # sum the values of S(fibs[k]) for k from 2 to 90
    for i in range(2, 90 + 1):
        res += S(fibs[i])
        res %=m
    
    return res


ans = solve()

print(f"{ans=}")
print(f"{time.time() - t} sec")
