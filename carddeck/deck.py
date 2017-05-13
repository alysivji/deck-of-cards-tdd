from collections import deque


class Card:
    '''Represents an individual playing card
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck(deque):

    def __init__(self):
        '''Create standard deck of card'''

        RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        SUITS = ['hearts', 'diamonds', 'spades', 'clubs']

        for suit in SUITS:
            for rank in RANKS:
                self.append(Card(suit=suit, rank=rank))
