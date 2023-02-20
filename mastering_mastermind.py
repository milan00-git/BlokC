import random
import itertools
from Mastermind_feedback import feedback
'''mastermind game'''

#list of colors for game
colors = ['a', 'b', 'c', 'd', 'e', 'f']

#gives length for color combination
length = 4

max_guesses = length + len(colors)

#all possible color combinations
permutation = [code for code in itertools.product(colors, repeat=length)]

def valid_guess(guess):
    '''decide if the guess is valid
    :return boolean
    :param string
    '''

    if guess == None:
        return False

    # check if guess is valid length
    if len(guess) != length:
        return False

    for pin in guess:

        if pin not in colors:
            return False

    #guess is valid
    return True
def reduceer(possibilities, vorige_gok, fb):
    '''
    Bepaal de mogelijkheden die nog over zijn na de laatste gok.
    :param array    Mogelijkheden die er nu nog zijn
    :param tuple    Vorige gok
    :param tuple    Feedback (zwart, wit)
    :return:
    '''
    nieuwe_mogelijkheden = []

    # test if the possibility is still possible
    for code in possibilities:
        #decide the feedback from the vorige_gok and the possibilities
        #and compare with the past given feedback
        if fb == feedback(vorige_gok, code):
            # code is still possible
            nieuwe_mogelijkheden.append(code)

    # give back new possibilities
    return nieuwe_mogelijkheden
def guess_input():

    #start with empty guess
    guess = None

    while not valid_guess(guess):
        print(f'that is not the right color or combination, choose colors: {colors}')
        guess_input = input('guess the color combination like: rbbg: ')

        #convert guess to a tuple
        guess = tuple(list(guess_input))

    return guess

def main():
    '''
    main game function (play the game)
    '''
    secret = random.choice(permutation)
    print(len(permutation))
    print(secret)

    #print the color options and the answer as test
    print('welcome in mastermind, your choice of colors from the list: ', colors)

    guess = guess_input()

    #number of guesses
    guesses_amount = 1

    #decide all possibilities
    possibilities = permutation.copy()

    while secret != guess and guesses_amount < max_guesses:
        #inform user
        print('color combination is not valid')
        print(f'u have {max_guesses - guesses_amount} attempts')

        #feedback
        zwart, wit = feedback(secret, guess)
        print(f'{zwart}, {wit}')

        #gives remaining possibilities
        possibilities = reduceer(possibilities, guess, (zwart, wit))
        print(len(possibilities))

        #let user guess again
        guess = guess_input()

        #amount of guesses wil get smaller
        guesses_amount += 1

    if secret == guess:
        #inform user
        print(f'u guessed the color in {guesses_amount} times, congrats!')
    else:
        print('game over, u have not guessed the code')

    #give user option to play the game again
    play = input('do u want to play the game again? [yes/no]')

    if play == 'yes':
        main()

#only runs the game if we want this specific script
if __name__ == '__main__':
    main()