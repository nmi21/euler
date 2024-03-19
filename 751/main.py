import time
from decimal import *

t = time.time()

# set the appropriate precision for decimal
c = getcontext()
c.traps[FloatOperation] = False
c.prec = 25


def next_vals(b):
    # generate the values for a(n+1), b(n+1)
    # given b(n)

    next_b = Decimal(int(b)) * (b - Decimal(int(b)) + 1)
    next_a = Decimal(int(next_b))

    return next_a, next_b


def tau_generator(theta):
    # generate a value for tau given an input of theta

    b1 = theta
    a1 = Decimal(int(b1))

    pair_list = [(a1, b1)]

    # save tuples to a list, using most recent value for b
    for i in range(25):
        a, b = next_vals(pair_list[-1][1])
        pair_list.append((a, b))

    # generate tau
    
    # pull just the a values
    t = [str(x[0]) for x in pair_list]
    
    # insert a decimal after the first number
    t.insert(1, ".")

    # join the string and then take proper numbers past decimal
    tau = "".join(t)
    tau = Decimal(tau[:26])

    return tau


def delta(theta, tau):
    # give the difference between theta and tau
    # if theta > tau, res < 0
    # if theta < tau, res > 0
    return tau - theta


def solve():
    
    # initialize theta and incrementer, inc
    theta = Decimal(2)
    inc = Decimal('.1')

    # initialize running conditions
    d = 1
    while d > 0:
        theta += inc
        tau = tau_generator(theta)
        d = delta(theta, tau)

        # if d is less than 0, we overshot
        # subtract the increment
        # change the increment, recalculate d
        if d < 0:
            theta -= inc
            inc /= 10
            d = delta(theta, tau)

    return str(theta)


ans = solve()

print(f"{ans=}")
print(f"{time.time() - t} sec")
