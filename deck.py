import random

SUITS = "Hearts", "Diamonds", "Spades", "Clubs"
RANKS = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card) 

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
if __name__ == "__main__":
    new_deck = Deck()
    new_deck.shuffle()
    card = new_deck.deal_one()
    print(card)