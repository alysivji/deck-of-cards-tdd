'''Tests for Blackjack
'''

from carddeck.deck import Card
from carddeck.blackjack import BlackjackHand

import pytest


def test_create_blackjackhand():
    hand = BlackjackHand()
    card1 = Card(suit='hearts', rank='K')
    card2 = Card(suit='hearts', rank='A')
    card3 = Card(suit='hearts', rank='A')

    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)
    hand_score = hand.score()

    assert hand_score == 12


@pytest.mark.parametrize('cards,expected_score', [
    ([('K', 'hearts'), ('A', 'hearts'), ('A', 'clubs')], 12),
    ([('K', 'hearts'), ('A', 'hearts')], 21),
    ([('A', 'hearts'), ('A', 'clubs')], 2),
    ([(5, 'hearts'), (6, 'hearts')], 11),
    ([(5, 'hearts'), (6, 'hearts'), ('A', 'spades')], 12),
    ([(2, 'diamonds'), (2, 'clubs')], 4),
])
def test_create_multiple_blackjack_hands(cards, expected_score):
    hand = BlackjackHand()

    for (rank, suit) in cards:
        card_dealt = Card(suit=suit, rank=rank)
        hand.add_card(card_dealt)

    assert hand.score() == expected_score
