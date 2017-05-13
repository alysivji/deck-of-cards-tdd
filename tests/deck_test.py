from carddeck.deck import Card, Deck


def test_create_card():
    new_card = Card(suit='hearts', rank=8)

    assert new_card.suit == 'hearts'
    assert new_card.rank == 8


def test_create_deck():
    deck = Deck()
    assert len(deck) == 52


def test_deck_deal():
    deck = Deck()
    card_dealt = deck.deal()

    assert card_dealt not in deck
    assert len(deck) == 51


def test_shuffle():
    deck = Deck()
    unshuffled_deck = deck.copy()
    deck.shuffle()

    assert deck != unshuffled_deck
