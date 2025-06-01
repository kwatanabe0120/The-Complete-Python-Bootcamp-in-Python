# ==== Game State ====
board = [' '] * 9            # status of board
test_board = ['0','1','2','3','4','5','6','7','8'] #For introduction
is_player1 = True            
winner_decided = False       
player1_marker = ''          
player2_marker = ''          

# Display current board
def display_board(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    print('\n')

# Decide which player use which marker
def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1, please choose your marker from X or O: ').upper()
        
    player1 = marker
    player2 = ''
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Starting game... Player1 = {player1}, Player2 = {player2}\n')
    return (player1, player2)

# Decide where to edit with validation
def player_placement(board):
    place = 'Wrong'

    while True:
        place = input('Please Enter the number to place your mark: ')
    
        if place not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid input. Please choose an empty spot on the board using numbers 0-8.")
        elif board[int(place)] != ' ':
            print("The place is already taken")
        else:
            return int(place)

# Change data in board with the marker based on the is_player1 variable 

def change_data(board, index):
    global is_player1
    marker = ''
    if is_player1:
        marker = player1_marker
        is_player1 = False
    else:
        marker = player2_marker
        is_player1 = True
    board[index] = marker


# Check if the game is won,tied, lost, or ongoing.
def check_condition(board):
    global winner_decided
    # Check columns
    for i in range(0,3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            print('\nYou win!\n')
            winner_decided = True
    # Check rows
    for i in [0,3,6]:
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            print('\nYou win!\n')
            winner_decided = True
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        print('\nYou win!\n')
        winner_decided = True
    if board[2] == board[4] == board[6] and board[2] != ' ':
        print('\nYou win!\n')
        winner_decided = True
    
    # Tie check
    if ' ' not in board:
        print('This game is a draw!\n')
        winner_decided = True
     
# Ask if players want to play again.
def reset_game():
    global winner_decided
    global board
    answer = ' '
    while answer != 'Yes' and answer != 'No':
        answer = input('Play again? Yes or No: ')
        if answer == 'Yes':
            winner_decided = False
            board = [' ']*9
        elif answer == 'No':
            print('Thank you for playing!')
        else:
            print('Please enter Yes or No')

# Introduction of Game
print('\nWelcome to Tic Toe game\nHere is the number for each space of the board\n')
display_board(test_board)
player1_marker, player2_marker = player_input()

# Repeat c and d until the game has been won or tied.
while not winner_decided:
    index = player_placement(board)
    change_data(board, index)
    display_board(board)
    check_condition(board)
    if winner_decided:
        reset_game()

