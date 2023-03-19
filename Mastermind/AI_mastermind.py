'''A.I voor mastermind game'''

'''
Gebruikte bronnen (zie README.md):
Alle bronnen uit readme
'''
# 1. adjust worst-case strategy to AABB
# 2. For own heuristics use the worst, worst-case strategy
# 3. simple and worst-case strategies don't give feedback in the form
# (1,0) or (4,0)
# 4. find a way to implement the algorithms in to the mastering_mastermind.py

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
    '''Select the combination with the worst worst-case score'''
    scores = {}
    for guess in combinations:
        # Keep track of the maximum minimum score across all feedbacks
        max_min_score = 0
        for feedback in evaluate(guess, secret):
            # Calculate the minimum score for this feedback
            min_score = len(combinations)
            for possible_secret in combinations:
                if evaluate(guess, possible_secret) != feedback:
                    # Eliminate the possible secret based on the feedback
                    combinations.remove(possible_secret)
                min_score = min(min_score, len(combinations))
                # Add the eliminated possible secret back to the list
                combinations.append(possible_secret)
            if min_score > max_min_score:
                max_min_score = min_score
        scores[guess] = max_min_score

    # Choose the guess with the minimum maximum score
    min_max_score = min(scores.values())
    for guess in combinations:
        if guess in scores and scores[guess] == min_max_score:
            return guess

def choose_strategy():
    choose = int(input('choose a strategy from 1 to 3: \n'
                   '1. simple strategy\n'
                   '2. worst case strategy\n'
                   '3. my heuristic\n'
                   'insert answer: '))

    if choose == 1:
        strategy = simple_strategy(combinations)
        return strategy

    elif choose == 2:
        strategy = worst_case_strategy(combinations)
        return strategy

    elif choose == 3:
        strategy = my_heuristic(combinations)
        return strategy

def play_game_ai():
    '''AI plays game'''

    combinations = all_combinations.copy()

    # amount of guesses made
    guesses_lst = []

    # amount of guesses for AI in 10 tries

    for amount in range(1, 10):
        guess = worst_case_strategy(combinations)
        guesses_lst.append(guess)
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

    return guesses_lst

play_game_ai()