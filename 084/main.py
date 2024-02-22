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

This is likely simple enough that we can simply model it

Each function should take in current location and output final location based on those


"""

import time
import random

t = time.time()

sides_on_dice = 6

location_names = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]


# dice roll
def roll_die(sides=6):
    return random.randint(1, sides)


# roll 2x dice and see if doubles
def dice_roll(sides=sides_on_dice, __print=False):
    # return sum of two die and if they were the same
    roll1 = roll_die(sides)
    roll2 = roll_die(sides)
    if __print:
        print(f"{roll1=}")
        print(f"{roll2=}")
    return roll1 + roll2, roll1 == roll2


def community_chest(current_location):
    # Community Chest (2/16 cards):
    #     Advance to GO
    #     Go to JAIL

    card = random.randint(1, 16)

    end_location = current_location

    if card == 1:
        end_location = location_names.index("GO")
    elif card == 2:
        end_location = location_names.index("JAIL")

    return end_location


def chance_card(current_location):
    
    """
    Chance (10/16 cards):
    -- Advance to GO
    -- Go to JAIL
    -- Go to C1
    -- Go to E3
    -- Go to H2
    -- Go to R1
    -- Go to next R (railway company)
    -- Go to next R
    Go to next U (utility company)
    Go back 3 squares.

    Chance locations
    """

    end_location = current_location

    if current_location == location_names.index("CH1"):
        next_railway = location_names.index("R2")
        next_utility = location_names.index("U1")
    elif current_location == location_names.index("CH2"):
        next_railway = location_names.index("R3")
        next_utility = location_names.index("U2")
    elif current_location == location_names.index("CH3"):
        next_railway = location_names.index("R1")
        next_utility = location_names.index("U1")

    card = random.randint(1, 16)

    if card == 1:
        end_location = location_names.index("GO")
    elif card == 2:
        end_location = location_names.index("JAIL")
    elif card == 3:
        end_location = location_names.index("C1")
    elif card == 4:
        end_location = location_names.index("E3")
    elif card == 5:
        end_location = location_names.index("H2")
    elif card == 6:
        end_location = location_names.index("R1")
    elif card == 7 or card == 8:
        # go to next railway
        end_location = next_railway
    elif card == 9:
        # go to next utility
        end_location = next_utility
    elif card == 10:
        # Go back 3 squares.
        end_location = current_location - 3

    return end_location


def move(start_location, consecutive_doubles):

    end_location = start_location
    double_counter = consecutive_doubles

    dice_sum, doubles = dice_roll()

    # deal with doubles
    if doubles:
        double_counter += 1
        if double_counter == 3:
            double_counter = 0
            end_location = location_names.index("JAIL")
            return end_location, double_counter
    else:
        double_counter = 0

    # not three in a row doubles
    end_location += dice_sum
    end_location %= 40

    # deal with G2J
    if end_location == location_names.index("G2J"):
        end_location = location_names.index("JAIL")
        return end_location, double_counter

    # deal with community chest
    community_chest_locations = [
        location_names.index("CC1"),
        location_names.index("CC2"),
        location_names.index("CC3"),
    ]
    if end_location in community_chest_locations:
        end_location = community_chest(end_location)

    # deal with chance cards
    chance_card_locations = [
        location_names.index("CC1"),
        location_names.index("CC2"),
        location_names.index("CC3"),
    ]
    if end_location in chance_card_locations:
        end_location = community_chest(end_location)

    return end_location, double_counter


def sim(limit=1_000_000, sides=6):
    
    loc_counter = {k: 0 for k in range(40)}

    location = 0
    d_counter = 0

    for _ in range(limit):
        location, d_counter = move(start_location=location, consecutive_doubles=d_counter)
        loc_counter[location] += 1

    chance_counter = {k: 100*v/limit for (k, v) in loc_counter.items()}

    return chance_counter


def solve(limit=1_000_000):
    chance = sim(limit)

    chance_dict = dict(sorted(chance.items(), key=lambda item:item[1], reverse=True))

    return chance_dict


ans = solve(1000000)
print(ans)


print(f"{time.time() - t}")
