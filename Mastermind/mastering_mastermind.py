'''mastermind game'''
'''Gebruikte bronnen (zie README.md):
Bron 1
'''
import random
import itertools

'''global variables'''
#list of colors for game
colors = ['r', 'b', 'c', 'g', 'o', 'p']

#gives length for color combination
length = 4

#max amount of guesses calculated
max_guesses = length + len(colors)

#all possible color combinations from the colors list and the length
permutation = [code for code in itertools.product(colors, repeat=length)]

def valid_guess(guess):
    '''
    defines what makes a guess valid

    :return boolean
    :param string
    '''

    # there is no given input for guess
    if guess == None:
        return False

    # the length of the input guess does not correspond to the length
    # given by the codemaker
    if len(guess) != length:
        print('code does not give back a valid length')
        return False

    # does the guess contain colors that come that are valid with variable colors?
    for pin in guess:
        # if the color is not in colors then code is invalid
        if pin not in colors:
            return False

    # guess is valid
    return True
def reduce(combinations, previous_guess, feedback):
    '''
    reduces the combinations that are left from the last guess

    :param array    remaining possibilities
    :param tuple    previous guess
    :param tuple    Feedback (black, white)
    :return:
    '''
    # list of new combinations
    new_combinations = []

    # test if the combination is still possible
    for code in combinations:

        # feedback from the previous_guess and the possibilities
        # compared with the past given feedback

        if feedback == evaluate(previous_guess, code):

            # code is still possible
            new_combinations.append(code)

    return new_combinations
def guess_input():

    #start with empty guess
    guess = None

    while not valid_guess(guess):
        print(f'that is not the right color or combination, choose colors: {colors}')
        guess_input = input('guess the color combination like: rbbg: ')

        #convert guess to a tuple
        guess = tuple(list(guess_input))

    return guess
def evaluate(guess,secret):
    '''
    :param guess:
    :param secret:
    :return:
    '''

    black, white = 0, 0
    used = []

    # The black pins
    for position in range(len(guess)):
        if guess[position] == secret[position]:
            black += 1
            used.append(position)

    # the white pins
    secret_copy = list(secret).copy()
    for position in used:
        secret_copy.remove(secret[position])

    for i in range(len(guess)):

        if i not in used:
            if guess[i] in secret_copy:
                white += 1
                secret_copy.remove(guess[i])

    return (black, white)

def main():
    '''
    main game function (play the game)
    '''

    # generates secret combination for codebreaker to guess
    secret = random.choice(permutation)
    print(len(permutation))

    # print answer for testing
    print(secret)

    # inform user for colors to choose from
    print('welcome in mastermind, your choice of colors from the list: ', colors)

    # call guess_input() inside this function
    guess = guess_input()

    # number of guesses start
    guesses_amount = 1

    # a copy of all possibilities given the color and length
    # for the game
    possibilities = permutation.copy()

    while secret != guess and guesses_amount < max_guesses:
        # inform user
        print('the code is not valid, try again')
        print(f'u have {max_guesses - guesses_amount} attempts')

        # gives feedback to user
        black, white = evaluate(guess, secret)
        print(f'{black}, {white}')

        # gives remaining possibilities
        possibilities = reduce(possibilities, guess, (black, white))
        print(f'u have {len(possibilities)} possibilities\n')

        # let user guess again
        guess = guess_input()

        # amount of guesses wil get smaller
        guesses_amount += 1

    if secret == guess:
        # inform user has won
        black, white = evaluate(guess, secret)
        print(f'{black}, {white}')
        print(f'u guessed the code in {guesses_amount} attemps, congrats!')
    else:
        # inform user has lost
        print('game over, u have not guessed the code')

    # give user option to play the game again
    play = input('do u want to play the game again? [yes/no]')

    # calls main() function if user wants to play game again ('yes')
    if play == 'yes':
        main()

# only runs the game if we want this specific script
if __name__ == '__main__':
    main()