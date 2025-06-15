import constraints

class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += constraints.values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

# for test
    def __str__(self):
        result = ''
        for card in self.cards:
            result += f'{card.rank} of {card.suit}\n'
        return result

import card

if __name__ == '__main__':
    test_hand = Hand()
    c1 = card.Card('Diamonds', 'Ace')
    c2 = card.Card('Diamonds', 'Three')
    c3 = card.Card('Diamonds', 'Queen')
    test_hand.add_card(c1)
    test_hand.add_card(c2)
    test_hand.add_card(c3)
    test_hand.adjust_for_ace()
    print(test_hand.value)
