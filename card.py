class Card:   # inherit from 'object'
    def __init__(self, rank, suit):
        self._rank = rank  # private instance variable
        self.suit = suit

    def get_rank(self):
        return self._rank

    @property
    def rank(self):  # getter property
        return self._rank

    @property
    def suit(self):  # getter property
        return self._suit

    @suit.setter
    def suit(self,value):
        if value in ('Clubs', 'Diamonds', 'Hearts', 'Spades', 'Joker'):
            self._suit = value
        else:
            raise ValueError(f"{value} is not a valid suit")

    def __repr__(self):   # code to create object
        return f"Card('{self.rank}', '{self.suit}')"

    def __str__(self):    # human-friendly info
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    card1 = Card("10", "Wombats")
    print(f"{card1 = }")   #  repr(card1)
    print(card1)    # str(card1)
    print(f"{card1.get_rank() = }")
    print(f"{type(Card.rank) = }")
    
    print(f"{card1.rank = }")
    print(f"{card1.suit = }")
    card1.suit = "Wombats"
    