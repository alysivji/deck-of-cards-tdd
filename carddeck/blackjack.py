'''Blackjack Module'''

import itertools
from carddeck.deck import Hand


class BlackjackHand(Hand):
    '''Main class with rules of Blackjack'''

    def score(self):
        letter_rank = {'J': 10, 'Q': 10, 'K': 10}
        ace_rank = [1, 11]
        num_aces = 0

        hand_value = 0

        # calculate hand value minus Aces
        for card in self:
            if card.rank == 'A':
                num_aces += 1
            elif isinstance(card.rank, str):
                hand_value += letter_rank[card.rank]
            else:
                hand_value += card.rank

        # add ace to hand
        possible_scores = \
            [sum(ace_score) + hand_value
             for ace_score in itertools.product(ace_rank, repeat=num_aces)]

        if max(possible_scores) <= 21:
            return max(possible_scores)
        else:
            return min(possible_scores)
