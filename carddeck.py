import random
from card import Card

class CardDeck:
    # class variables
    _RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    _SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self._SUITS:
            for rank in self._RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
        # handle empty deck

    def __len__(self):  # implement len(carddeck-object)
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{len(self)}"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}()"

    @classmethod
    def ranks(cls):
        return cls._RANKS

if __name__ == "__main__":
    cd1 = CardDeck()
    cd1.shuffle()
    print(cd1)
    print(f"{cd1 = }")
    print(f"{cd1.cards = }\n")
    for _ in range(5):
        card = cd1.draw()
        print(card, repr(card))
    print(f"{CardDeck.ranks() = }")
    print(f"{cd1.ranks() = }")
    