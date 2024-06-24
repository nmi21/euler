"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k;
for example, R(6) = 111111.

Given that n is a positive integer and gcd(n, 10) = 1, it can be shown that there always exists a value,
k, for which R(k) is divisible by n, and let A(n) be the least such value of k;
for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.

--
Method:

First, we need to understand what A(n) is.

If we look at A(7)...
We are curious which values of R(k) have 7 as a factor
R(1) = 1                                        not divisible by 7
R(2) = 11                                       not divisible by 7
R(3) = 111 = 3 * 37                             not divisible by 7
R(4) = 1111 = 11 * 101                          not divisible by 7
R(5) = 11111 = 41 * 271                         not divisible by 7
R(6) = 111111 = 3 * 7 * 11 * 13 * 37            divisible by 7!!!
Thus, A(7) = k value for the first time 7 is a factor, which is 7.

They also give us a hint that if gcd(n, 10) does not equal 1, n will not factor into R(k).
This is obvious, but it means we do not need to check for values of n if n % 2 or % 5 == 0

- write a function that calculates the first value of k for when R(k) % n == 0
- cycle through that function until k > 10 ** 6

Some mod math on R(k) % n == 0
R(k) = (10**k - 1) / 9
Thus...
R(k) % n == 0
(10**k - 1) / 9 % n == 0
(10**k - 1) % 9*n == 0
10**k % 9*n == 1

So we can check if n divides R(k) by checking: 10**k % 9*n == 1.

This will take a long time for larger values of k, and so we can write ways to check that very quickly using some
mod tricks: modular exponentiation. See function: binary_modular_exponentiation

Also noteworthy is that n >= k.


"""
import time
import math


t = time.time()


# Write a function that can easily calculate base^exponent % modulus if exponent is large
def binary_modular_exponentiation(base, exponent, modulus):
    """
    A much more efficient version of modular_exponentiation.
    :param base:
    :param exponent:
    :param modulus:
    :return: (base ^ exponent) % modulus
    """
    if modulus == 1:
        return 0

    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result


# Write a function that calculates if n is a factor of R(k)
def check_factor_of_rk(n, k):
    """
    Check to see if R(k) % n == 0
    :param n:
    :param k:
    :return: R(k) % n == 0
    """

    b = 10
    e = k
    m = 9*n

    return binary_modular_exponentiation(b, e, m) == 1




# Write a function that determines the lowest value of R(k) for a given n
# start with 



def determine_a_of_n(limit):
    """
    takes in a value of n and returns the first value of k for which R(k) % n == 0; that is n is a divisor of R(k)
    note that k > n
    :param n:
    :return:
    """
    n = limit

    running = True
    while running:

        # check the condition that gcd(n, 10) == 1 else continue
        if math.gcd(n, 10) == 1:

            # start at k = 1, cycle through values of k
            k = 1

            while True:
                # if n is a factor of R(k), break and go to next value of n, else increment k
                if check_factor_of_rk(n, k):
                    break

                k += 1

                # if here
                if k > limit:
                    res = n
                    running = False

        n += 1

    return res




a_of_n, k = determine_a_of_n(10)
print(a_of_n)
print(k)


"""
To solve this, we should note that n is a factor of R(k) when n >= k
So, for something like 1,000,000, we only need to start looking at values of 
"""


# start with the limit we are searching for and set to n
# go through different values of n, checking to make sure that gcd(n, 10) == 1
# if gcd(n, 10) == 1, set a value l = 1
# loop through values of l

# start with a value at your limit
# check to see if it is in any R(k) values prior to your limit
# if it exceeds your limit -- done!
# if not, check the next value of n

# check to make sure gcd(n, 10) = 1
# get the value for A(n)
# check if value is above threshold; if yes --> break
# if not, go to next value of n


"""
Time required to complete each value for i:
i == 0 took 4.9591064453125e-05 sec
i == 1 took 0.00011110305786132812 sec
i == 2 took 0.0030488967895507812 sec
i == 3 took 0.11571383476257324 sec
i == 4 took 11.353179931640625 sec

"""


print(f"{time.time() - t} sec")
