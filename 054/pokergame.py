from pokerhand import PokerHand


class Poker:

    def __init__(self, hands):
        self.p1_hand = PokerHand(hands[0])
        self.p2_hand = PokerHand(hands[1])
        self.p1_result = self.p1_hand.result
        self.p2_result = self.p2_hand.result
        self.winner = self.get_winner()

    def get_winner(self):
        for key in self.p1_result:
            if self.p1_result[key] > self.p2_result[key]:
                return 1
            elif self.p1_result[key] < self.p2_result[key]:
                return 2
            elif self.p1_result[key] == self.p2_result[key]:
                if key == 'high card':
                    return 0
                continue
            else:
                return -1
