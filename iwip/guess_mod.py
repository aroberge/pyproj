''' Modified version from http://inventwithpython.com/guess.py

* Renamed variables according to PEP8
* Kept lines below 80 characters long
* Used the prompt argument of input()
* Use if/elif/else rather than a series of if
* Removed unneeded comments
* Use += shortcut
* Added a function to ensure integer values are passed to input() when
  required

'''

import random

def valid_input(message):
    '''Ensures that integer value is provided to input'''
    while True:
        try:
            guess = int(input(message))
            return guess
        except ValueError:
            print("You must enter an integer value. ")

guesses_taken = 0
my_name = input('Hello! What is your name? ')
number = random.randint(1, 20)
print('Well, {}, I am thinking of a number between 1 and 20.'.format(my_name))

while guesses_taken < 6:
    guess = valid_input('Take a guess. ')
    guesses_taken += 1

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print('Good job, {}!'.format(my_name), end=' ')
    print('You guessed my number in {} guesses!'.format(guesses_taken))
else:
    print('Nope. The number I was thinking of was {}.'.format(number))
