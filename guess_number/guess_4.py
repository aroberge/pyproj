''' Guess the number

Building on the previous version, save the results (number of games and
total number of guesses) in a file named "guessing_game.stats"
in the user's home directory.

The file should be updated each time this program is executed.

You may find os.path.expanduser("~") useful.
'''

import random
import os

max_nb = 100
prompt = "Guess a number, between 1 and {}, or enter -1 to quit:".format(max_nb)
file_name = "guessing_game.stats"
file_path = os.path.join(os.path.expanduser("~"), file_name)


def init():
    '''retrieve information from file if it exists'''

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            info = f.readline().split()
    else:
        return 0, 0

    nb_games = int(info[0])
    guesses = int(info[1])
    return nb_games, guesses


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


def game():
    '''A single game

       The number of guesses made is returned if a successful guess was
       made - otherwise the return value is False
    '''
    nb_attempts = 0
    number = random.randint(1, max_nb)
    while True:
        guess = safe_input()
        nb_attempts += 1
        if guess == number:
            print("Congratulations, you guessed correctly.")
            print("You only needed {} attempts.".format(nb_attempts))
            return nb_attempts
        elif guess == -1:
            print("Sorry to see you leave; the number was {}.".format(number))
            return False
        elif guess < number:
            print("    Your guess is too low.\n")
        elif guess > number:
            print("    Your guess is too high.\n")


def goodbye(nb_games, total_attempts):
    '''provide feedback to player included average number of attempts
       required if at least one game was played.
    '''
    if nb_games != 0:
        print("You have guessed {} numbers in {} attempts.".format(
              nb_games, total_attempts))
        print("The average number of guesses per game was {}.".format(
              total_attempts/nb_games))
        with open(file_path, 'w') as f:
            f.write("{} {}".format(nb_games, total_attempts))
    print("Goodbye and thanks for playing")


def play_games():
    '''play multiple games, keeping track of the total number of games played
       and the total number of attempts made to guess a number
    '''

    nb_games, total_attempts = init()
    if nb_games == 0:
        print("Welcome to the Guessing Game!\n")
    else:
        print("Welcome back to the Guessing Game!\n")

    while True:
        result = game()
        if result:
            total_attempts += result
            nb_games += 1
            ans = input("Another game? 'y' to continue, anything else to quit.")
            if ans != 'y':
                break
        else:
            break

    goodbye(nb_games, total_attempts)


if __name__ == '__main__':
    play_games()
