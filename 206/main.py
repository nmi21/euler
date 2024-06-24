"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Method:
- Only the final few numbers will affect the final few digits. 
- E.g. if we had a number nxxxxx, there is no way that n will 
affect the final digit of nxxxxx ** 2

- So, given our inputs we know that the last digit is "0" 
because the final digit in the square is "0".

- Given that the last digit is "0", we know the last two digits in the 
square are "00" (because any number ending in zero squared will have two 
zeroes at the end).

- Of the digits remaining in the square, we now need to figure out how to get 9_0. 
We know that it is actually 900. So the the square % 1000 == 900. In order to get 
the 900, we need to find a number, n < 10, that when squared % 10 == 9. There are 
only two available numbers for that: n = 3 (n^2 == 9) or n = 7 (n^2 == 49).

- Ultimately, we need to figure out which numbers to check
The smallest number is 1020304050607080900
The largest number is 192939495969798990

The difference of the square roots is approx 3.8 * 10^8

If we only check numbers n that when n % 100 == 30 or n % 100 == 70,
then we are only checking 2 numbers in every 100 (1 in 50)

So then we are checking 3.8 * 10^8 / 50 = 7.6*10^6
7.6 million numbers is easy enough to brute force check

"""

import time
import math

t = time.time()


def check_num(n):
    
    checker = 9
    while checker > 1:
        
        n = n // 100
        
        if n % 10 != checker:
            return False
        
        checker -= 1
    
    return True


def solve():
    original = "1_2_3_4_5_6_7_8_9_0"

    # get the minimum value (replace _ with 0)
    min_val = int(original.replace("_", "0"))

    # get the max val (replace _ with 9)
    max_val = int(original.replace("_", "9"))

    # start search at min val, but find closest num where last digits are 00
    min_n = int(math.sqrt(min_val))
    max_n = int(math.sqrt(max_val))

    start = min_n - (min_n % 100)
    end = max_n

    for i in range(start, end, 100):
        for j in [30, 70]:
            num = i + j
            if check_num(num ** 2):
                return num
    
    return None


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t} sec")
