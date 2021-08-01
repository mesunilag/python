
class Card:
    
    def __init__(self, suite, value):
        if suite not in ('Hearts', 'Diamonds', 'Clubs', 'Spades'):
            raise ValueError("Incorrect value for suite!")
        elif value not in ('A','2','3','4','5','6','7','8','9','10','J','Q','K'):
            raise ValueError("Invalid value for value!")
        self._suite = suite
        self._value = value
        pass
    
    def __repr__(self):
        return f"{self._value} of {self.suite}"

class Deck:
    def __init__(self, cards,deck_size=52):
        self.deck_size = deck_size 
        self.cards = cards
        
    
    def count(self):
        return len(self.cards)
    
    def __repr__(self):
        return f"Deck of {self.deck_size} cards"
    
    def _deal(self, num):
        if not self.cards:
            raise ValueError("All cards have been dealt")
        elif len(self.cards) < len(num):
            return [ self.cards.pop() for c in range(0, len(self.cards))]
        else:
            return [ self.cards.pop() for c in range(0, len(num))]
    
    def shuffle(self):
        if len(self.cards) < self.deck_size:
            raise ValueError("Only full decks can be shuffled")
        else:
            from random import shuffle
            shuffle(self.cards)
            
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, num):
        return self._deal(num)        
    
    
class CardDeckApp:
    