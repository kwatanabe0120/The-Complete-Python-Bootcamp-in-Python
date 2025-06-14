import constants

class Card:
    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = constants.values[rank]

    def __str__(self):
        return self.rank + ' of '+ self.suit
