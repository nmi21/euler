"""
Each of the six faces on a cube has a different digit (0 to 9)
written on it; the same is done to a second cube. By placing
the two cubes side-by-side in different positions we can form
a variety of two digit numbers.

For example, the square number 64 could be formed:
    6   4

In face, by carefully choosing the digits on both cubes it is 
possible to display all fo the square numbers below one-hundred:
01, 04, 09, 16, 25, 49, 64, 81

For example, one way this can be achieved is by placing 
{0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other
cube.

However, for this problem we shall allow the 6 or 9 to be turned 
upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and
{1, 2, 3, 4, 6, 7} allows for all nine square numbers to be 
displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the 
digits on each cube, not the order

    {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
    {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two
distinct sets in the last example both represent the extended
set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit
numbers.

How many distinct arrangements of the two cubes allow for all of 
the square numbers to be displayed?

--

Method
- we have 10 digits to choose from, and 6 to choose
    - 10 choose 6
        n = 10
        r = 6
        n! / r!(n-r)! = 210 possible selections per dice
    - two dice so 210^2 = 44100 possibilities
- create all 44100 possible selections of dice




"""

import time
import itertools

t = time.time()


def check_dice(die1, die2):
    # for a given pair of dice: die1 and die2
    # check to see if you can make all perfect squares

    perfect_squares = set([
        (0, 1),
        (0, 4),
        (0, 9),
        (1, 6),
        (2, 5),
        (3, 6),
        (4, 9),
        (6, 4),
        (8, 1)
    ])

    # create copies and add necessary 6 or 9
    cube1 = set(die1)
    cube2 = set(die2)

    if 6 in cube1:
        cube1.add(9)
    if 9 in cube1:
        cube1.add(6)
    
    if 6 in cube2:
        cube2.add(9)
    if 9 in cube2:
        cube2.add(6)


    # form all possible cube combinations
    cube1 = list(cube1)
    cube2 = list(cube2)
    cube_combos = []
    for c1 in cube1:
        for c2 in cube2:
            cube_combos.append((c1, c2))
            cube_combos.append((c2, c1))
    
    # remove valid combos from remaining squares
    for combo in cube_combos:
        if combo in perfect_squares:
            perfect_squares.remove(combo)

    # if there are no valid combos left,
    # then you can make all of the perfect squares
    return len(perfect_squares) == 0


def solve():
    # create all dice combinations
    # search over unique combinations
    # test to see if that combination works

    # - on the first pass I counted double the required number
    # - this is because die1, die2 = x, y 
    # was counted differently than die1, die2 = y, x
    # - but at the end of the day that is the same combination of dice
    # - we could either divide the end result by 2,
    # or we could reduce our search space

    # create all combinations
    dice_combos = list(itertools.combinations(range(10), 6))

    counter = 0
    for i in range(len(dice_combos)):
        for j in range(i + 1, len(dice_combos)):
            if check_dice(dice_combos[i], dice_combos[j]):
                counter += 1

    return counter


ans = solve()
print(f"{ans=}")
print(f"{time.time() - t} sec")

