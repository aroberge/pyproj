''' Guess the number

Adapting version 4 to use easygui_qt instead of terminal to interact
with user.

'''

import random
import os
import easygui_qt as easy

# The lazy way: redefining print which is not possible with Python 2!
print = easy.show_message

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


def game():
    '''A single game

       The number of guesses made is returned if a successful guess was
       made - otherwise the return value is False
    '''
    nb_attempts = 0
    number = random.randint(1, max_nb)
    while True:
        guess = easy.get_int("Choose a number or click 'Cancel' to quit",
                              min_=1, max_=max_nb)
        nb_attempts += 1
        if guess is None:
            print("Sorry to see you leave; the number was {}.".format(number))
            return False
        elif guess == number:
            print("Congratulations, you guessed correctly.")
            print("You only needed {} attempts.".format(nb_attempts))
            return nb_attempts
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
            ans = easy.get_string("Another game? 'y' to continue, anything else to quit.")
            if ans != 'y':
                break
        else:
            break

    goodbye(nb_games, total_attempts)


if __name__ == '__main__':
    play_games()
