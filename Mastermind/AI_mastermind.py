'''A.I voor mastermind game'''

'''
Gebruikte bronnen (zie README.md):
Alle bronnen uit readme
'''

from mastering_mastermind import *
import random

'''global variables'''
# color variable from mastermind.py
colors_ai = colors

# length of color combination from mastermind.py
length_ai = length

# all possible color combinations from the colors list and the length from mastermind.py
all_combinations = permutation
print(f'{len(all_combinations)} possible combinations\n')

# returns a random combination of colors as secret.
# k = parameter in random.choices for defining the length of the variable (length)
secret = tuple(random.choices(colors, k=length))
print(f'secret code: {secret}\n')

# def my_heuristic(combinations):
#     scores = {}
#     # looping over combinations
#     for guess in combinations:
#         # guess index in scores gives minimum value from combinations
#         #
#         scores[guess] = min([len(reduce(combinations, guess, feedback)) for feedback in evaluate()])
#
#     # gives back worst, worst-case
#     return max(scores, key=scores.get)
# print(my_heuristic())
def my_heuristic(combinations):
    '''Select the combination with the largest partition element'''
    scores = {}
    for guess in combinations:
        partitions = {tuple(sorted([x for i, x in enumerate(guess) if i != j])) for j in range(length)}
        score = max(len(reduce(combinations, partition, feedback)) for partition in partitions
                    for feedback in evaluate(guess, secret))
        scores[guess] = score
    return max(scores, key=scores.get)

def simple_strategy(combinations):
    # Return the first combination in sorted order that has not been eliminated
    sorted_combinations = sorted(all_combinations)

    # Return the first combination that hasn't been eliminated
    for combination in sorted_combinations:
        if combination in combinations:
            return combination

def worst_case_strategy(combinations):
    """
        Selects the combination with the worst worst-case score.
        """
    scores = {}
    for guess in combinations:
        max_score = 0
        for feedback in evaluate(guess, secret):
            score = len(reduce(combinations, guess, feedback))
            if score > max_score:
                max_score = score
        scores[guess] = max_score
    return min(scores, key=scores.get)

def play_game_ai():
    '''AI plays game'''

    combinations = all_combinations.copy()

    # amount of guesses for AI in 10 tries

    for amount in range(1, 10):
        guess = simple_strategy(combinations)
        feedback = evaluate(guess, secret)

        black, white = evaluate(guess, secret)
        print(f'guess {amount}: {guess}, feedback: ({black}, {white})')

        if feedback == (length, 0):
            print(f'Found answer {guess} in {amount} guesses')
            break

        # reduces the amount of combinations with each guess if answer is not found
        combinations = reduce(combinations, guess, feedback)
    else:

        # AI game over
        print(f'Could not find answer. Answer was {secret}.')
        black, white = evaluate(guess, secret)
        print(f'feedback: {black}, {white}')

    return guess

play_game_ai()