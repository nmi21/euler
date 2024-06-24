"""
https://projecteuler.net/problem=205

--

Method:
- First, we need to calculate the probability that Peter rolls any
available number
- Second, we need to calculate the probability that Colin rolls any
available number
- For each number that Peter rolls, we multiply the
    - probability of Peter rolling that number by the
    - probability of Colin rolling any number lower
- For example,
    - Peter rolls a 10:
        - P(PP > CC) = P(PP | 10) * (P(CC | 6) + P(CC | 7) + 
        P(CC | 8)) + P(CC | 9)
    - The probability of a tie would be multiplying the chance that
    each of them gets 10
    - The probability of Colin winning would be the product sum for 
    any case where Colin scores higher than Peter
    - This needs to be repeated for each number
"""

import time
import itertools

t0 = time.time()


def dice_counter(num_dice, sides_on_dice):
    """
    Returns
    
    dictionary where key: value is
        key == sum of roll
        value == number of rolls that achieves sum
    """

    dice_dict = {}
    for roll in itertools.product(range(1, sides_on_dice + 1), repeat=num_dice):
        dice_dict[sum(roll)] = dice_dict.get(sum(roll), 0) + 1

    return dice_dict


def dice_game(player1_rolls, player2_rolls):
    """
    Returns dictionaries with probability for p1 wins, p2 wins, and ties at each dice sum value
    """

    p1_win = {}
    p2_win = {}
    ties = {}

    p1_total = sum(player1_rolls.values())
    p2_total = sum(player2_rolls.values())

    # for each value that p1 rolls
    for p1_val, p1_count in player1_rolls.items():
        
        # grab the probability of p1_val
        prob_p1_val = p1_count / p1_total

        # To see the win probability:
        # - get the probability of p2_val being less than p1_val
        # - multiply together
        prob_p1_win = sum([v for k, v in player2_rolls.items() if k < p1_val]) / p2_total
        p1_win[p1_val] = prob_p1_val * prob_p1_win

        # To see the tie probability
        # - get the probability of p1_val == p2_val
        ties[p1_val] = prob_p1_val * player2_rolls.get(p1_val, 0)

        # To see the win probability for p2
        # - get the probability of p2 val being greater than p1_val
        # - multiply together
        prob_p2_win = sum([v for k, v in player2_rolls.items() if k > p1_val]) / p2_total
        p2_win[p1_val] = prob_p1_val * prob_p2_win

    return p1_win, p2_win, ties
        
        
def solve():

    peter_dice_qty = 9
    peter_dice_sides = 4
    peter = dice_counter(peter_dice_qty, peter_dice_sides)

    colin_dice_qty = 6
    colin_dice_sides = 6
    colin = dice_counter(colin_dice_qty, colin_dice_sides)

    peter_wins, colin_wins, ties = dice_game(peter, colin)

    return round(sum(peter_wins.values()), 7)


ans = solve()
print(f"{ans=}")

print(f"{time.time() - t0} sec")
