def display_board(board):
    print(f"{board[0] or ' '} | {board[1] or ' '} | {board[2] or ' '}")
    print("--+---+--")
    print(f"{board[3] or ' '} | {board[4] or ' '} | {board[5] or ' '}")
    print("--+---+--")
    print(f"{board[6] or ' '} | {board[7] or ' '} | {board[8] or ' '}")

def user_placement():
    result = 'default'
    while True:
        result = input('Enter number to place (0-8)')

        if result.isdigit() == False:
            print('Please Enter digit')
            continue
        
        if int(result) not in range(0,9):
            print('Please enter from 0 to 8')
        else:
            return int(result)

# odd num is for O, even for X
is_letter_O = 1

def write_data(board,index):
    global is_letter_O
    letter = 'O' if is_letter_O % 2 == 0 else 'X'
    board[index] = letter
    is_letter_O +=1


def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != '':
            print('You Win!!')
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != '':
            print('You Win!!')
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != '':
        print('You Win!!')
        return True
    if board[2] == board[4] == board[6] and board[2] != '':
        print('You Win!!')
        return True

    # No winner
    return False



board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
example_board = ['0','1','2','3','4','5','6','7','8']
winner_decided = False

print('\nWelcome to Tic Tac Toe game!\nHere is the numer for each place')
display_board(example_board)

while winner_decided == False:
    place =user_placement()
    write_data(board, place)
    display_board(board)
    winner_decided = check_winner(board)