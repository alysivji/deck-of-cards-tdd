from carddeck.deck import Card, Deck, Hand
import pytest


##################
# Card Class Tests
##################

def test_create_card():
    new_card = Card(suit='hearts', rank=8)

    assert new_card.suit == 'hearts'
    assert new_card.rank == 8


##################
# Deck Class Tests
##################

@pytest.fixture
def deck():
    return Deck()


def test_deck_size(deck):
    assert len(deck) == 52


def test_deal_single_card_from_deck(deck):
    card_dealt = deck.deal()

    assert card_dealt not in deck
    assert len(deck) == 51


def test_shuffle_deck(deck):
    unshuffled_deck = deck.copy()
    deck.shuffle()

    assert deck != unshuffled_deck


def test_deal_hand(deck):
    hands = deck.deal_hands(num_players=5, num_cards=3)
    assert len(hands) == 5
    assert len(hands[0]) == 3

    # dealing more cards than possible
    with pytest.raises(ValueError):
        hands = deck.deal_hands(num_players=53, num_cards=1)


##################
# Hand Class Tests
##################

@pytest.fixture
def make_test_hand():
    hand = Hand()

    card1 = Card(suit='hearts', rank=3)
    card2 = Card(suit='spades', rank=8)
    card3 = Card(suit='spades', rank='A')
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)

    return hand


def test_create_empty_hand():
    hand = Hand()
    assert len(hand) == 0


def test_create_hand_with_multiple_cards(make_test_hand):
    hand = make_test_hand
    assert len(hand) == 3


def test_score_hand(make_test_hand):
    '''Get score... default implementation gets max card (Aces high)'''
    hand = make_test_hand
    hand_score = hand.score()

    assert hand_score == 14
