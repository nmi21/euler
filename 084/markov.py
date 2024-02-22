"""
https://projecteuler.net/problem=84

In the game, Monopoly, the standard board is set up in the following way:

[see image from website]

A player starts on the GO square and adds the scores on two 6-sided dice to determine 
the number of squares they advance in a clockwise direction. Without any further rules 
we would expect to visit each square with equal probability: 2.5%. However, landing on 
G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go 
directly to jail, if a player rolls three consecutive doubles, they do not advance the 
result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on 
CC or CH they take a card from the top of the respective pile and, after following the 
instructions, it is returned to the bottom of the pile. There are sixteen cards in each 
pile, but for the purpose of this problem we are only concerned with cards that order 
a movement; any instruction not concerned with movement will be ignored and the player 
will remain on the CC/CH square.

Community Chest (2/16 cards):
    Advance to GO
    Go to JAIL
Chance (10/16 cards):
    Advance to GO
    Go to JAIL
    Go to C1
    Go to E3
    Go to H2
    Go to R1
    Go to next R (railway company)
    Go to next R
    Go to next U (utility company)
    Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of 
finishing on it is zero, the CH squares will have the lowest probabilities, as 
5/8 request a movement to another square, and it is the final square that the 
player finishes at on each roll that we are interested in. We shall make no 
distinction between "Just Visiting" and being sent to JAIL, and we shall also 
ignore the rule about requiring a double to "get out of jail", assuming that they 
pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can 
concatenate these two-digit numbers to produce strings that correspond with sets 
of squares.

Statistically it can be shown that the three most popular squares, in order, are 
JAIL (6.24%) = Square 10, 
E3 (3.18%) = Square 24, and 
GO (3.09%) = Square 00. 
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

--
Method:

For each location, calculate the probability of getting to any other location
Create a 40x40 matrix where each (r, c) is the probability that you can get to c from r

Dealing with doubles
- For any given time, you have a 1/6 chance of rolling doubles
- Two get 2x consecutive doubles, that is 1/6 * 1/6 = 1/36
- to get 3x consecutive doubles, that is 1/6 * 1/6 * 1/6 = 1/216
- which means that regardless of where you are on the board, you will have a 1/216 chance of 
going to jail in addition to whatever other chances you have

location_names = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]
community_chest_locations = [2, 17, 33]

After the dice roll
markov[0] = [
    0,    0,    1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 
    3/36, 2/36, 1/36, 0,    0,    0,    0,    0,    0,    0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

"""

import time
import itertools
from fractions import Fraction
import numpy as np
import pdb

t = time.time()


def markov_monopoly(dice_sides=6):
    location_names = [
        "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
        "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
        "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
        "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
    ]


    transition = [[0] * 40 for _ in range(40)]
    rows = len(transition)
    cols = len(transition[0])


    # deal with standard rolls
    total_combos = 0
    combo_counter = {}
    for die1, die2 in itertools.product(range(1, dice_sides+1), repeat=2):
        dice_sum = die1 + die2
        if dice_sum in combo_counter:
            combo_counter[dice_sum] += 1
        else:
            combo_counter[dice_sum] = 1
        total_combos += 1
    for r in range(rows):
        for roll, count in combo_counter.items():
            c = r + roll
            c %= 40
            transition[r][c] = Fraction(count, total_combos)


    # deal with doubles
    chance_jail_from_doubles = Fraction(1, dice_sides**3)
    chance_standard_roll = 1 - chance_jail_from_doubles
    for r in range(rows):
        for c in range(cols):
            transition[r][c] *= chance_standard_roll
        transition[r][10] += chance_jail_from_doubles


    # deal with community chest
    community_chest_locations = []
    for square in location_names:
        if square.startswith("CC"):
            community_chest_locations.append(location_names.index(square))
    cc_jail = Fraction(1, 16)
    cc_go = Fraction(1, 16)
    cc_stay = 1 - cc_jail - cc_go
    for r in range(rows):
        for cc in community_chest_locations:
            # jail 
            transition[r][10] += cc_jail * transition[r][cc]
            # go
            transition[r][0] += cc_go * transition[r][cc]
            #stay
            transition[r][cc] *= cc_stay


    # deal with chance card
    chance_card_locations = []
    railway_locations = []
    utility_locations = []
    for square in location_names:
        if square.startswith("CH"):
            chance_card_locations.append(location_names.index(square))
        elif square.startswith("R"):
            railway_locations.append(location_names.index(square))
        elif square.startswith("U"):
            utility_locations.append(location_names.index(square))
    next_railway_loc = {}
    railway_and_cc = sorted(chance_card_locations + railway_locations)
    railway_and_cc.append(railway_and_cc[0])
    next_utility_loc = {}
    utility_and_cc = sorted(chance_card_locations + utility_locations)
    utility_and_cc.append(utility_and_cc[0])
    for cc_loc in chance_card_locations:
        railway_ind = railway_and_cc.index(cc_loc) + 1
        next_railway_loc[cc_loc] = railway_and_cc[railway_ind]
        utility_ind = utility_and_cc.index(cc_loc) + 1
        next_utility_loc[cc_loc] = utility_and_cc[utility_ind]

    chance_straight_jumps = ["GO", "JAIL", "C1", "E3", "H2", "R1"]
    for r in range(rows):
        for ch in chance_card_locations:
            
            # deal with straight jumps
            for jump in chance_straight_jumps:
                c = location_names.index(jump)
                transition[r][c] += transition[r][ch] * Fraction(1, 16)
            
            # deal with next railway
            next_railway = next_railway_loc[ch]
            transition[r][next_railway] += transition[r][ch] * Fraction(2, 16)

            # deal with next utility
            next_utility = next_utility_loc[ch]
            transition[r][next_utility] += transition[r][ch] * Fraction(1, 16)
        
            # deal with move back 3 places
            transition[r][ch - 3] += transition[r][ch] * Fraction(1, 16)

            # deal with stay in chance
            transition[r][ch] *= Fraction(6, 16)


    # deal with "go to jail"
    g2j = location_names.index("G2J")
    jail = location_names.index("JAIL")
    for r in range(rows):
        for c in range(cols):
            transition[r][jail] += transition[r][g2j]
            transition[r][g2j] = 0
    transition[g2j] = [0] * cols
    transition[g2j][jail] = Fraction(1, 1)

    # transfer to numpy array
    transition_np = np.array(transition)

    # cast as float
    transition_np = transition_np.astype(float)

    # transpose
    transition_np = transition_np.T

    # normalize by column
    transition_np = transition_np / transition_np.sum(axis=0)

    # verify that all columns add to 1
    if not np.allclose(transition_np.sum(axis=0), 1.0):
        print("not close to 1")

    # pull eigenvalues, eigenvectors
    eigen_val, eigen_vec = np.linalg.eig(transition_np)

    # find the eigenvalue closest to 1
    index = np.argmin(np.abs(eigen_val - 1))

    # normalized eigenvector is steady state values
    steady = np.real(eigen_vec[:, index]) / np.sum(np.real(eigen_vec[:, index]))

    # form into a dictionary
    steady_dict = {k: round(100*v, 2) for k, v in enumerate(steady)}

    # sort by values
    sorted_probabilities = {k: v for k, v in sorted(steady_dict.items(), key=lambda item: item[1], reverse=True)}
    print()
    print(f"{sorted_probabilities=}")

    top_three = [str(x) for x in list(sorted_probabilities)[:3]]

    ans = ""
    for top in top_three:
        if len(top) < 2:
            top = "0" + top
        ans += top

    return ans


six_sides = markov_monopoly()
print(f"{six_sides=}")

four_sides = markov_monopoly(dice_sides=4)
print(f"{four_sides=}")

print(f"{time.time() - t} sec")
