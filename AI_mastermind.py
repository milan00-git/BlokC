'''A.I voor mastermind game'''

'''
Gebruikte bronnen:
- nummer 3, 4 en 5 uit README.md (zie bronvermelding github)
'''

from mastering_mastermind import *
import itertools
import random

# color variable from mastering_mastermind
colors_ai = colors
# length of color combination
length_ai = length
def generate_all_feedbacks(length):
    '''Generate all possible feedback combinations for a given length'''
    feedbacks = []
    for black in range(length+1):
        for white in range(length+1):
            if black + white <= length:
                feedbacks.append((black, white))
    return feedbacks

all_combinations = list(itertools.product(colors, repeat= length))
all_feedbacks = generate_all_feedbacks(length)

def strategies(combinations, strategy):
    '''Make a guess based on the remaining possibilities and the given strategy'''
    if strategy == "simple":
        # return random.choice(combinations) # random strategy
        nextguess = combinations[0]
        return nextguess

    elif strategy == "worst-case_strategy":
        scores = {}
        for guess in combinations:
            scores[guess] = min([len(reduce(combinations, guess, fb)) for fb in all_feedbacks])
        return max(scores, key=scores.get)

def play_game_ai(strategy):
    '''AI plays game'''

    secret = tuple(random.choices(colors, k=length))
    combinations = list(itertools.product(colors, repeat=length))
    guesses = []
    for i in range(10):
        guess = strategies(combinations, strategy)
        guesses.append(guess)
        feedback = evaluate(guess, secret)

        if feedback == (length, 0):
            print(f'Found answer {guess} in {i+1} guesses')
            break
        combinations = reduce(combinations, guess, feedback)
    else:
        print(f'Could not find answer. Answer was {secret}.')
    return guesses

# Play a game using the simple strategy
print("Playing game with simple strategy")
random_guesses = play_game_ai("simple")

print("\nsimple strategy guesses:")
print(random_guesses)

# play game using the worst-case strategy
print('\nplaying game with worst-case strategy')
random_guesses = play_game_ai('worst-case_strategy')

print('\nWorst-case strategy guesses: ')
print(random_guesses)