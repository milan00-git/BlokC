'''A.I voor mastermind game'''

'''
Gebruikte bronnen:
- nummer 3, 4 en 5 uit README.md (zie bronvermelding github)
'''
# 1. adjust worst-case strategy to AABB
# 2. For own heuristics use the worst, worst-case strategy
# 3. simple and worst-case strategies don't give feedback in the form
# (1,0) or (4,0)

from mastering_mastermind import *
import random

'''global variables'''
# color variable from mastermind.py
colors_ai = ['r', 'b', 'c', 'g', 'o', 'p']
# length of color combination from mastermind.py
length_ai = 4
# all possible color combinations from the colors list and the length from mastermind.py
all_combinations = permutation
print(f'{len(all_combinations)} possible combinations\n')
# returns a random combination of colors as secret.
# k = parameter in random.choices for defining the length of the variable (length)
secret = tuple(random.choices(colors, k=length))
print(f'secret code: {secret}')

# def generate_all_feedbacks(length):
#     '''Generate all possible feedback combinations for a given length'''
#     feedbacks = []
#     for black in range(length+1):
#         for white in range(length+1):
#             if black + white <= length:
#                 feedbacks.append((black, white))
#     return feedbacks
#
# all_feedbacks = generate_all_feedbacks(length)
# print(f'all possible feedbacks {all_feedbacks}')

def heuristic(combinations):
    scores = {}
    for guess in combinations:
        scores[guess] = min([len(reduce(combinations, guess, feedback)) for feedback in all_feedbacks])
    return max(scores, key=scores.get)
def simple_strategy():
    # sorted_combinations = all_combinations.sort()
    sorted_combinations = sorted(all_combinations)
    for combination in sorted_combinations:
        nextguess = combination[0]
        if nextguess == secret:
            return combination

def play_game_ai():
    '''AI plays game'''

    guesses = []

    # amount of guesses for AI in 10 tries
    for amount in range(10):
        guess = simple_strategy()
        guesses.append(guess)
        feedback = evaluate(guess, secret)

        if feedback == (length, 0):
            print(f'Found answer {guess} in {amount+1} guesses')
            break

        # reduces the amount of combinations with each guess if answer is not found
        combinations = reduce(combinations, guess, feedback)
    else:

        # AI game over
        print(f'Could not find answer. Answer was {secret}.')

    return guesses

# Play a game using the simple strategy
print("Playing game with simple strategy")
simple = play_game_ai(simple_strategy())

print("\nsimple strategy guesses:")
print(simple)

# play game using the worst, worst-case strategy
print('\nplaying game with heuristic')
heuristic = play_game_ai(heuristic())

print('\nheuristic guesses: ')
print(heuristic)