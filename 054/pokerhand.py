card_vals = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
card_vals = [str(x) for x in card_vals]


def get_card_value(v):
    return 2 + card_vals.index(v)


class PokerHand:
    """
    Takes in a list of 5 cards and determines how the hand scores.
    The attribute result is a list of the following form:
    """

    def __init__(self, hand):
        self.hand = hand  # hand is a sequence of 5 cards
        self.sort_hand()
        self.vals = self.get_vals()
        self.high_card = self.get_high_card()
        self.result = self.get_result()

    def sort_hand(self):
        self.hand = [[get_card_value(i[0]), i[1]] for i in self.hand]
        self.hand.sort()

    def get_vals(self):
        return [x[0] for x in self.hand]  # just get the card values

    def get_high_card(self):
        return self.vals[4]

    # determines if it is a flush (all cards are of the same suit)
    def is_flush(self):
        """
        :return: Boolean
        """
        suits = [x[1] for x in self.hand]
        return all(suit == suits[0] for suit in suits)

    # function to determine if it is a straight (all cards are sequential)
    def is_straight(self):
        """
        Will return the value of the highest card in the straight if it is a straight.
        Otherwise, will return 0
        """
        if all((self.vals[i-1] + 1) == self.vals[i] for i in range(1, 5)):
            return self.high_card
        else:
            return 0

    def is_straight_flush(self):
        """
        Will return the value of the highest card in the straight if it is a straight flush.
        Otherwise, will return 0
        """
        if self.is_straight() and self.is_flush():
            return self.high_card
        else:
            return 0

    def is_royal_flush(self):
        """
        Returns a boolean: if it is a Royal Flush or not
        """
        return self.is_straight_flush() and self.high_card == 14

    def get_result(self):
        result = {
            'royal flush': self.is_royal_flush(),
            'straight flush': self.is_straight_flush(),
            'four of a kind': 0,
            'full house': 0,
            'flush': self.is_flush(),
            'straight': self.is_straight(),
            'three of a kind': 0,
            'two pairs': 0,
            'one pair': 0,
            'high card': self.high_card
        }

        uniques = [*set(self.vals)]
        uniques.sort()
        for key in uniques:
            num_cards = self.vals.count(key)
            if num_cards == 4:
                result['four of a kind'] = key
            elif num_cards == 3:
                result['three of a kind'] = key
            elif num_cards == 2:
                if result['one pair']:
                    result['two pairs'] = key
                result['one pair'] = key

        if result['three of a kind'] and result['one pair']:
            result['full house'] = result['three of a kind']

        return result
