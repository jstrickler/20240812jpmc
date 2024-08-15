from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for i in (1, 2):
            card = Card("Joker", f"Joker")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(f"{j.cards = }")
    
    print(f"{j = }\n")
    
    for _ in range(5):
        print(j.draw())
    