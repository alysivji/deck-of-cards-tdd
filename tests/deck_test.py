from carddeck.deck import Card, Deck


def test_create_card():
    new_card = Card(suit='hearts', rank=8)

    assert new_card.suit == 'hearts'
    assert new_card.rank == 8


def test_create_deck():
    deck = Deck()
    assert len(deck) == 52
