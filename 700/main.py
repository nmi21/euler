"""
Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4503599627370517.

An element of this sequence is defined to be an Eulercoin if it is 
strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first 
Eulercoin. The second term is 3008341430083414 which is greater than 
1504170715041707 so is not an Eulercoin. However, the third term is 
8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins.

--

Method:
- we cannot go through and check every number, there 16 digits in the number!
- notice that the mod number is prime, and therefore each value for k * coin1 % m 
will be unique for k: [0, m-1]
- find the first few coins:
    
    coin #1
    n=1
    coin = 1504170715041707
    
    coin #2
    n=3
    coin = 8912517754604

    coin #3
    n=506
    coin = 2044785486369

    coin #4
    n=2527
    coin = 1311409677241

    coin #5
    n=4548
    coin = 578033868113

    coin #6
    n=11117
    coin = 422691927098

    coin #7
    n=17686
    coin = 267349986083

    coin #8
    n=24255
    coin = 112008045068

    coin #9
    n=55079
    coin = 68674149121

    coin #10
    n=85903
    coin = 25340253174

    coin #11
    n=202630
    coin = 7346610401

    coin #12
    n=724617
    coin = 4046188430

    coin #13
    n=1246604
    coin = 745766459

    coin #14
    n=6755007
    coin = 428410324

    coin #15
    n=12263410
    coin = 111054189

    coin #16
    n=42298633
    coin = 15806432

- We can calculate the first several coins relatively quickly, but it gets much tougher after that.
- My system found the first 14 in less than a second, but then it took 10s to get to #16.
- However, we can use modular multiplicative inverse:

    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    So essentially there is a value of x such that ax % m = 1.

    There is a fun implication to this and modular arithmetic in general, 
    which is to say that we can multiply both sides by a constant and expect it to hold true.

    i.e.: 
        k * a * x % m = k * 1
        k * a * x % m = k

    e.g.:
        a = 3 m = 11
        thus, x = 4:
            3 * 4 % 11 = 1
        
        let k = 2:
            k * a * x % m  = k
            2 * 3 * 4 % 11 = k
                6 * 4 % 11 = k
                   24 % 11 = 2
    
- This will allow us to check each number (1, 2, 3, etc...) to see if it is an euler coin,
because we will know if the value for k is less than those found for the k value of the last euler coin (1)

"""

import time
import math

t = time.time()

coin1 = 1504170715041707
m = 4503599627370517


def mod_mult_inv(a, m):
    """
    Returns the modular multiplicative inverse of a % m
    That is, there is a value, x, such that ax % m == 1
    """
    
    # I know that you can use the native pow(a, b, mod) function
    # and set b = -1 to find the modular multiplicative inverse
    # but this is slightly more fun
    
    # use Extended Euclidean algorithm:
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers

    # ax + my = gcd(a, m)
    z = math.gcd(a, m)
    
    old_r, r = a, m
    old_s, s = 1, 0
    
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s
        
    
    x = old_s + m
    x %= m
    
    return x 


coins = [coin1]

# find the first handful of Euler coins
temp = coin1
n = 2
while len(coins) < 16:
    temp += coin1
    temp %= m
    if temp < coins[-1]:
        coins.append(temp)
    n += 1

# check all of values starting at 1 and moving up
stop_ind = coins[-1]
inv = mod_mult_inv(coin1, m)
prev_ind = inv
for k in range(1, stop_ind):
    temp_ind = k * inv % m
    if temp_ind <= prev_ind:
        coins.append(k)
        prev_ind = temp_ind

ans = sum(coins)

print(f"{ans=}")
print(f"{time.time() - t} sec")
