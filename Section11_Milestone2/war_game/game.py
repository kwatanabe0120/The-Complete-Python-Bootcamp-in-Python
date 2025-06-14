import deck
import player


# Game setup
player1 = player.Player('One')
player2 = player.Player('Two')

new_deck = deck.Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())


game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # Check if plays have cards or not
    if len(player1.all_cards) == 0:
        print('Player One, out of cards!\nPlayer Two win!')
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print('Player Two, out of cards!\nPlayer One win!')
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player1.remove_one())

    player_two_cards = []
    player_two_cards.append(player2.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)            
            player1.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player2.add_cards(player_one_cards)            
            player2.add_cards(player_two_cards)

            at_war = False
        
        else:
            print('War!')

            if len(player1.all_cards) < 5:
                print('Player one unable to declear war')
                print('Player Two wins!')
                game_on = False
                break

            elif len(player2.all_cards) < 5:
                print('Player two unable to declear war')
                print('Player One wins!')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player1.remove_one())
                    player_two_cards.append(player2.remove_one())

