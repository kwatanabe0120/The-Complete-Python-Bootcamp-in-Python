
def display_game_list(game_list):
    print("Current game list:")
    print(game_list)
    print('\n')

def position_choice():
    choice = 'Wrong'
    while True:
        choice = input("Please enter a position (0, 1, or 2): ")
        if choice not in ['0', '1', '2']:
            print("Invalid input. Please enter 0, 1, or 2.")
            continue
        return int(choice)
    
def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def game_choice():
    choice = 'Wrong'
    while choice not in ['Y','N']:
        choice = input("Do you want to continue? (Y/N): ").upper()
        if choice not in ['Y', 'N']:
            print("Invalid input. Please enter Y or N.")
    if choice == 'Y':
        return True
    else:
        print("Thank you for playing!")
        return False


game_list= [0,1,2]
game_on = True

while game_on:
    display_game_list(game_list)
    position = position_choise()
    game_list = replacement_choise(game_list, position)
    display_game_list(game_list)

    game_on = game_choice()
