# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# Guess the number game.

import random 

print('Hello. What is your name?')
name = input()
        
print('Well, {}, I am thinking of a number between 1 and 20'.format(name))
secret_number = random.randint(1, 20)

for guess_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break

if guess == secret_number:
    print('Good job {}! You guessed my number in {} guesses!'.format(name, guess_taken))
else:
    print('Nope. The number I was thinking was {}'.format(secret_number))
