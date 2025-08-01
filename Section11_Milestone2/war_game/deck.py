import random
import constants
import card

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in constants.suits:
            for rank in constants.ranks:
                created_card = card.Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()