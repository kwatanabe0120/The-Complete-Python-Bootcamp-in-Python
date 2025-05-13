from random import shuffle

def shuffle_list(l):
    shuffle(l)
    return l

def user_guess():
    response = ''
    while response not in ['0','1','2']:
        response = input('Pick from 0, 1 or 2')
    return int(response)

def check_answer(shuffledl, guess):
    if shuffledl[guess] == 'O':
        print('Correct!')
    else:
        print('try again!')
        print(shuffledl)

l = [' ','O',' ']

shuffeldl = shuffle_list(l)

anser = user_guess()

check_answer(shuffeldl, anser)

