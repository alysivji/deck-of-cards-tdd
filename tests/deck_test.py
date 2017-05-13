from carddeck import deck


def test_create_deck():
    new_deck = deck.Deck()
    assert len(new_deck) == 52
