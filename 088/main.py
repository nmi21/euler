"""
A natural number, N, 
that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ..., ak},
is called a product-sum number:
    N = a1 + a2 + ... + ak = a1 + a2 + ... + ak

For example, 
6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. 
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows:

k = 2: 4 = 2 * 2 = 2 + 2
k = 3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k = 4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k = 5: 8 = 1 * 1 * 2 * 2 * 2 =  1 + 1 + 2 + 2 + 2
k = 6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; 
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is 
{4, 6, 8, 12, 15, 16}, the sum is 61
.

What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000
"""

"""
Notes:
- no prime number can be a product-sum number
    - because a prime, P, only has 2 divisors: 1 and P. At minimum, the sum of those two numbers is > P
- for any even k, 2*k is a product sum number (though not necessarily the smallest)
    - N = 2*k = k + 2 + 1 + 1 + ... + 1 = k * 2 * 1 * 1 * ... * 1
- every composite number makes up a product-sum number N (though not necessarily the smallest):
    - N = x * y * 1 * 1 * ... * 1
    - N = x + y + 1 + 1 + ... + 1

Method:
- determine the numbers (min, max) that need to be checked to make sure that all values for k are covered
    - remove the prime numbers
- for each number, get its factors
    - remove the identity multiplication x = x * 1 because it will not be a product sum number
    - these are the last in the list in my implementation
- from the factors, determine the product-sum set size by subtracting the sum of the factors
    - e.g. product-sum == 8
        factors = [2, 2, 2], [2, 4]
            8 - sum(factors[0]) + len(factors[0]) = 8 - 6 + 3 = 5
            8 - sum(factors[1]) + len(factors[1]) = 8 - 6 + 2 = 4
- with all of those calculated, determine the product-sum number for each set size
- sum the unique values from that set
"""

import math
import time

t = time.time()


def get_factorizations(lim):
    # get factors of all numbers up to and including limit
    # does not include 1 in identity factorization
    # for example, all primes will only include themselves
    # e.g. res[5] = [5]
    # the result is a list of lists

    # Method:
    # check the divisors of the number
    # create a list of empty lists for the factors of 0 and 1
    # starting at 3, iterate through all numbers up to the limit
    # for each number under investigation, create an empty list
    # start at 2 and go to the sqrt of the limit
    # if the number is divisible, add its factorizations to the list of possible factors

    factorizations = [[], [], [[2]]]

    for num in range(3, lim + 1):
        factors = []
        for div in range(2, int(math.sqrt(num) + 1) + 1):
            if num % div == 0:
                sub_factors = factorizations[num // div]
                for sub in sub_factors:
                    temp = sub[:]
                    temp.append(div)
                    factors.append(sorted(temp))
        factors.append([num])
        
        factorizations.append(factors)

    return factorizations
                

def get_prodsum_set_length(prodsum, factor_list: list):
    # take in a factor list and return the prodsum length

    return prodsum - sum(factor_list) + len(factor_list)


def solve(n):

    # get the factorizations for all numbers up to 2*n (see posits)
    fs = get_factorizations(2*n)

    # fill a dictionary with all of the possible product-sum set lengths behind a product-sum key
    ps_dict = {}
    for num, facs in enumerate(fs):
        if len(facs) > 1:
            ps_dict[num] = []
        else:
            continue

        # remove the identity factorization
        for f in facs[:-1]:
            ps_dict[num].append(get_prodsum_set_length(num, f))


    # create a dictionary where
    # key == product-sum set length
    # value == minimum number for given key
    min_dict = {}
    for key, val in ps_dict.items():
        for v in val:
            if v > n:
                continue
            if v not in min_dict:
                min_dict[v] = key
            elif key < min_dict[v]:
                min_dict[v] = key
    
    # pull all of the values into a list
    min_list = [0] * len(min_dict)
    for ind, x in enumerate(min_dict.values()):
        min_list[ind] = x

    return sum(set(min_list))


ans = solve(12_000)
print(f"ans == {ans}")
print(f"{time.time() - t} sec")
