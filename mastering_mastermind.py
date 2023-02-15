import random
import itertools

'''
To do:

- kleur gokken 
- feedback geven als kleur niet in combinatie voor komt maar wel op goede plek, 
als kleur wel voorkomt maar niet op de juiste plek, 
als kleur niet voorkomt en ook niet op goede plek. 
- Bot maken die ook met speler kan spelen
- eventueel UI maken met tkinter (optioneel) als er tijd voor is
'''

#list of colors
colors = ['r', 'y', 'b', 'g', 'p', 'c', 'o', 'v']

#holds the answer of the color combination
answer = []
length = 4

#alle mogelijkheden van combinaties kleuren
permutation = [code for code in itertools.product(colors, repeat=length)]
print(permutation)
print(len(permutation))

#random kleuren combinatie genereren
for i in range(0, length):
    answer.append(random.choice(colors))

print('choice of colors from the list: ', colors)
print(answer)

#first guess from user
guess = input('guess the color combination: ')

while answer != guess:

    if guess == answer:
        break

    elif len(guess) != len(answer):
        print('have u entered 4 colors?')

    else:
        print(f'that is not the right color, u can choose from the following colors: {colors}')

    guess = input('guess the color combination: ')

print('u guessed the color, congrats!')


def code_feedback(answer, gok):
    goed, bijnagoed = 0, 0

    # Kopieer de codes om te kunnen bewerken
    gok, answer = list(gok).copy(), list(answer).copy()

    # Vervang alle exacte matches door een plusje
    for i in range(length):
        if answer[i] == gok[i]:
            answer[i], gok[i] = '+', '+'
            goed += 1

    # Als de kleur ergens anders in de code zit telt hij als
    # bijna goed
    for j in range(length):
        if (gok[j] != '+') and (gok[j] in answer):
            bijnagoed += 1

    return (goed, bijnagoed)

# Damian's versie van de feedbackfunctie
def generate_feedback(combo, gok):
    # Starter feedback if no letters are correct
    feedback = [0, 0]
    # Check every letter in the combination
    for i in range(length):
         # If the letter is in the right spot
        if combo[i] == gok[i]:
            feedback[0] += 1
            feedback[1] -= 1
        # If the letter is in the wrong spot
        elif combo[i] in gok:
            feedback[1] += 1
    if feedback[1] < 0:
        feedback[1] = 0
    return feedback

# Frequentiefunctie
def freq(lijst):
    f = {}

    for element in lijst:
        # Tel 1 op bij de huidige frequentie van het element (default 0)
        f[element] = f.get(element, 0) + 1

    return f

combinaties = [x for x in itertools.product(colors, repeat=length)]
print(len(combinaties))

feedbackAAA = [code_feedback(combi, ['A', 'A', 'A']) for combi in combinaties]
feedbackAAB = [code_feedback(combi, ['A', 'A', 'B']) for combi in combinaties]
feedbackABC = [code_feedback(combi, ['A', 'B', 'C']) for combi in combinaties]

print(freq(feedbackAAA))
print(freq(feedbackAAB))
print(freq(feedbackABC))