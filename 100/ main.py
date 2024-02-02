"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
P(BB) = (15/21) x (14/20) = 1/2

The next such arrangement, for which there is exactly 50% change of taking blue discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1_000_000_000_000 discs in total, 
determine the number of blue discs that the box would contain.

-- 
Method:
- Let 
    b = number of blue discs
    n = total number of discs (red + blue)

- P(BB) =   b     b - 1     1
           --- * ------- = ---
            n     n - 1     2

            2 * b * (b - 1) = n * (n - 1)

            2b^2 - 2b = n^2 - n

            2b^2 - 2b - n^2 + n = 0

            2b^2 - 2b + (-n^2 + n) = 0

            use quadratic equation... {A = 2; B = -2; C = -n^2 + n}
            we don't need the -sqrt option

            b = (2 + sqrt(B^2 - 4AC))/(2A)

            b = (2 + sqrt((-2)^2 - (4)(2)(-n^2 + n)))/(2(2))

            b = (2 + sqrt(4 - (8)(-n^2 + n)))/4

            b = (2 + sqrt(4 + 8n^2 - 8n)))/4

            b = (2 + sqrt(4)sqrt(1 + 2n^2 - 2n)))/4

            b = (2 + 2*sqrt(1 + 2n^2 - 2n)))/4

            b = 2*(1 + sqrt(1 + 2n^2 - 2n)))/4

            b = (1 + sqrt(1 + 2n^2 - 2n)))/2

            we know that sqrt(1 + 2n^2 - 2n) needs to be rational for b to be rational
            rearrange to 2n^2 - 2n + 1...
            for it to be rational, it needs to be a perfect square
            set 2n^2 - 2n + 1 = y^2 where y^2 is our perfect square
            Now solve for n in terms of y: n(y)

            2n^2 - 2n + 1 = y^2

            2n^2 - 2n + 1 - y^2 = 0

            use quadratic equation {A = 2; B = -2; C = 1 - y^2}
            we don't need the -sqrt option

            n = (2 + sqrt((-2)^2 - 4(2)(1 - y^2))) / (2(2))

            n = (2 + sqrt(4 - 8*(1 - y^2))) / 4

            n = (2 + sqrt(4)sqrt(1 - 2*(1 - y^2))) / 4

            n = (2 + 2*sqrt(1 - 2*(1 - y^2))) / 4

            n = (1 + sqrt(1 - 2*(1 - y^2))) / 2

            n = (1 + sqrt(1 - 2 + 2y^2))) / 2

            n = (1 + sqrt(2y^2 - 1))) / 2

            Again,we know that sqrt(2y^2 - 1) needs to be rational
            So sqrt(2y^2 - 1) = x
            2y^2 - 1 = x^2
            rearrange...

            x^2 - 2y^2 = -1

            This is the form of the negative Pell equation, 
            for which there are recurrance generator functions!

            Given the fundamental solution for (x, y) = (1, 1)...

            x[n] = 3*x[n-1] + 4*y[n-1]
            y[n] = 2*x[n-1] + 3*y[n-1]

            With that, we can find successive values for (x, y)
            Knowing y, we can calculate n
            Once we find the correct number for n, we can calculate b!

"""

import math
import time

t = time.time()

LIMIT = 10 ** 12

def next_pell_sol(x = 1, y = 1):
    # generate the next pair of (x, y) for negative Pell's equation
    # negative Pell's equation takes the following form:
    #   x^2 - 2*y^2 = -1
    # default, that is next_pell_sol() has auto inputs for the fundamental solution (1, 1)
    # so default will give the second solution

    return 3*x + 4*y, 2*x + 3*y


# initialize values for x, y, and n
x, y = 1, 1
n = 0

# continue searching for values where n < LIMIT and stop when you do
while n < LIMIT:
    x, y = next_pell_sol(x, y)
    n = int((1 + math.sqrt(2*(y**2) - 1)) / 2)

    print(f"total_tiles={n}")

    # calculate blue tiles given total tiles, n
    blue_tiles = int((1 + math.sqrt(1 + (2*(n**2)) - 2*n))/2)
    print(f"{blue_tiles=}")

    red_tiles = n - blue_tiles
    print(f"{red_tiles=}")

    print()



print(f"{time.time() - t} sec")
