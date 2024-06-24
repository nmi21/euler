"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of
eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of
queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next
highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?

"""

from pokergame import Poker
from pokerhand import PokerHand

# extract each game
with open(file="p054_poker.txt", mode="r") as f:
    games = [line.strip() for line in f.readlines()]
# print(games)

game_results = {
    'p1_wins': 0,
    'p2_wins': 0,
    'tie': 0,
    'error': 0
}

# extract each player's hand
hands = [[game.split()[0:5], game.split()[5:]] for game in games]
# print(hands)
for hand in hands:
    p = Poker(hand)

    if p.winner == 1:
        game_results['p1_wins'] += 1
    elif p.winner == 2:
        game_results['p2_wins'] += 1
    elif p.winner == 0:
        game_results['tie'] += 1
    elif p.winner == -1:
        game_results['error'] += 1
    else:
        print(f"unexpected result: {p.winner}")

    # print(hand)
    # print(p.p1_result)
    # print(p.p2_result)
    # print(p.winner)
    # print()

ans = game_results['p1_wins']
print(f"ans == {ans}")
