'''Tests for Blackjack
'''

from carddeck.deck import Card
from carddeck.blackjack import BlackjackHand


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
