import constraints
import card
import random


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in constraints.suits:
            for rank in constraints.ranks:
                self.deck.append(card.Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    

if __name__ == '__main__':
    test_deck = Deck()
    # show all 52 cards
    print(test_deck)

    # Delete 51 cards
    for _ in range(51):
        test_deck.deal()
    
    # since pop method take away the last card so only one card at the top of deck will show
    print(test_deck)