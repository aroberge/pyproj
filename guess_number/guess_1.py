''' Guess the number

Have the computer select an integer between 1 and 10 (inclusive)
and ask the user to guess that number.

Then tell the user if they guessed right or not, and exit the program.
'''

import random

number = random.randint(1, 10)
guess = int(input("Guess a number, between 1 and 10: "))
if guess == number:
    print("Congratulations, you guessed correctly.")
else:
    print("Sorry, the number was {}.".format(number))
