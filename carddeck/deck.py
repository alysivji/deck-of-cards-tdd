from collections import deque
import random


class Card:
    '''Individual playing card'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __len__(self):
        return len(self)

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
                card = self.deal()
                hand.add_card(card)

        return player_hands


class Hand(list):
    '''Cards player is holding'''

    def add_card(self, card):
        self.append(card)

    def score(self):
        '''Get a score for the hand

        Default class will get max rank with Ace high'''

        letter_rank = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        ranks = max([card.rank if isinstance(card.rank, int) else letter_rank[card.rank] for card in self])

        return ranks
