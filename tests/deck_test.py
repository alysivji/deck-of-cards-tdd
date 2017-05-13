from carddeck.deck import Card, Deck, Hand
import pytest


###################
## Card Class Tests
###################

def test_create_card():
    new_card = Card(suit='hearts', rank=8)

    assert new_card.suit == 'hearts'
    assert new_card.rank == 8


###################
## Deck Class Tests
###################

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
        hands =  deck.deal_hands(num_players=53, num_cards=1)


###################
## Hand Class Tests
###################

def test_create_hand():
    hand = Hand()
