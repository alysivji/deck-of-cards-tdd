from carddeck import card


def test_create_card():
    '''Create card'''

    new_card = card.Card(suit='hearts', rank=8)

    assert new_card.suit == 'hearts'
    assert new_card.rank == 8
