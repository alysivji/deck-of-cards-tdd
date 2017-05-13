from collections import deque
import random


class Card:
    '''Represents an individual playing card
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __len__(self):
        return 1

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __eq__(self, other):
        if self.suit == other.suit:
            if self.rank == other.rank:
                return True

        return False


class Deck(deque):

    def __init__(self, *args, **kwargs):
        '''Create standard deck of card'''

        RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        SUITS = ['hearts', 'diamonds', 'spades', 'clubs']

        for suit in SUITS:
            for rank in RANKS:
                self.append(Card(suit=suit, rank=rank))

    def deal(self):
        '''Deal single card'''
        return self.popleft()

    def shuffle(self):
        '''Shuffle deck in place'''
        random.shuffle(self)


class Hand:

    def __init__(self):
        pass
