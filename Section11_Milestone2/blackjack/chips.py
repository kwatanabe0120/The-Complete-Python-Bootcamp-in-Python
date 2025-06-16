class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# For debugging
    def __str__(self):
        return f'You have total {self.total}, betting {self.bet}'
        
if __name__ == '__main__':
    test_chips = Chips()
    print(test_chips)

    test_chips.bet += 10000
    print(test_chips)