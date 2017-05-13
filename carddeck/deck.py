from collections import deque
import random


class Card:
    '''Individual playing card'''

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
    '''Deck of cards'''

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

    def deal_hands(self, num_players, num_cards):
        '''Deal cards to players
        
        Args
            num_players - num of players to deal to
            num_cards - num cards each player gets

        Returns
            list of Hand objects
        '''

        total_cards_to_deal = num_players * num_cards

        if total_cards_to_deal > 52:
            raise ValueError("Not enough cards to deal")

        # set up empty hand
        player_hands = []
        for _ in range(num_players):
            player_hands.append(Hand())

        # deal each card
        for _ in range(num_cards):
            for hand in player_hands:
                hand.append(self.deal())

        return player_hands


class Hand(list):
    '''Cards player is holding'''

    def __init__(self):
        pass
