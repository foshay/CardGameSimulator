
import random
from models.card import Card

class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self, shuffled=False):
        self.cards = [Card(suit, rank) for suit in self.SUITS for rank in self.RANKS]
        self.original_cards = self.cards.copy()
        if shuffled:
            self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def getOriginal(self):
        return self.original_cards

    def size(self):
        return len(self.cards)

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)
    