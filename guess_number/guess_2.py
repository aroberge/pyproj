''' Guess the number

Have the computer select an integer between 1 and 100 (inclusive)
and ask the user to guess that number.

Keep track of the user's number of guesses required to guess the correct value.

Provide feedback to the user indicating if their guess is too low or too high.

Make sure that incorrect input by the user (for exemple: entering a word
instead of number) are taken care of with appropriate feedback
given to the user.

Allow the user to leave the game at any time by entering a value of -1.

End the program by giving the user appropriate feedback; for example, if the
user guesses correctly, indicate how many guesses were needed.
'''

import random

# use a variable to avoid having to change the maximum value at
# two different places - if we decide to make the game more difficult.
max_nb = 100
number = random.randint(1, max_nb)
prompt = "Guess a number, between 1 and {}, or enter -1 to quit:".format(max_nb)


def safe_input():
    '''Prompts the user for an integer and return only when a valid value
       is entered
    '''
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print("You must enter a valid value.")


nb_attempts = 0
while True:
    guess = safe_input()
    nb_attempts += 1
    if guess == number:
        print("Congratulations, you guessed correctly.")
        print("You only needed {} attempts.".format(nb_attempts))
        break
    elif guess == -1:
        print("Sorry to see you leave; the number was {}.".format(number))
        break
    elif guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
