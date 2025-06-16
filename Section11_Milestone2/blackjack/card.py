class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit



if __name__ == '__main__':
    test_card = Card('Diamond', 'Ace')
    print(test_card)
