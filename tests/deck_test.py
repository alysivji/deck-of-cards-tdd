from carddeck.deck import Card, Deck
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


def test_create_deck(deck):
    assert len(deck) == 52


def test_deck_deal(deck):
    card_dealt = deck.deal()

    assert card_dealt not in deck
    assert len(deck) == 51


def test_shuffle(deck):
    unshuffled_deck = deck.copy()
    deck.shuffle()

    assert deck != unshuffled_deck
