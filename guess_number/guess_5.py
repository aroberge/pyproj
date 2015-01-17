''' Guess the number

Building on the previous version, save the results (number of games and
total number of guesses) in a database file named "guessing_game.db"
in the user's home directory.

The file should be updated each time this program is executed.
'''

import random
import sqlite3

max_nb = 100
prompt = "Guess a number, between 1 and {}, or enter -1 to quit:".format(max_nb)
db_file_name = "guessing_game.db"


def create_db():
    '''Creates a database file with the required basic structure'''
    try:
        db = sqlite3.connect(db_file_name)
        cursor = db.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS
            stats(name TEXT, nb_games INTEGER, nb_guesses INTEGER)
            ''')
        db.commit()
    except Exception as e:  # I am not experienced enough with databases
                            # to know what type of problem could occur here -
                            # hence the general catch all exception.
        db.rollback()
        raise e
    finally:
        db.close()


def retrieve_data():
    '''retrieves nb_games and nb_guesses from default player
       if it exists, otherwise returns 0 for both values.  In addition,
       returns boolean indicating whether or not the data existed.
    '''
    create_db()
    db = sqlite3.connect(db_file_name)
    cursor = db.cursor()
    cursor.execute('''SELECT name, nb_games, nb_guesses FROM stats''')
    stats = cursor.fetchone()  # retrieve the first row
    db.close()
    if stats is None:
        print("\n    This is your first game! \n")
        return 0, 0, False
    else:
        print("""     So far you have played {} games
            and required {} guesses on average""".format(
            stats[1], stats[2]/stats[1]))
        return stats[1], stats[2], True


def save_data(nb_games, nb_guesses, data_exists):
    '''saves the relevant data, updating the database if the
       information was already present, inserting it otherwise
    '''
    db = sqlite3.connect(db_file_name)
    cursor = db.cursor()
    if data_exists:
        cursor.execute('''UPDATE stats SET nb_games = ? WHERE name = ?
            ''', (nb_games, "player"))
        cursor.execute('''UPDATE stats SET nb_guesses = ? WHERE name = ?
            ''', (nb_guesses, "player"))
    else:
        cursor.execute('''INSERT INTO stats(name, nb_games, nb_guesses)
            VALUES(:name, :nb_games, :nb_guesses)''',
            {'name': "player", 'nb_games': nb_games, 'nb_guesses': nb_guesses})
    db.commit()
    db.close()


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


def goodbye(nb_games, total_attempts, data_exists):
    '''provide feedback to player included average number of attempts
       required if at least one game was played and, if the statistics
       were updated, saves the new values.
    '''
    if nb_games != 0:
        print("You have guessed {} numbers in {} attempts.".format(
              nb_games, total_attempts))
        print("The average number of guesses per game was {}.".format(
              total_attempts/nb_games))
        save_data(nb_games, total_attempts, data_exists)
    print("Goodbye and thanks for playing")


def play_games():
    '''play multiple games, keeping track of the total number of games played
       and the total number of attempts made to guess a number
    '''

    nb_games, total_attempts, data_exists = retrieve_data()
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

    goodbye(nb_games, total_attempts, data_exists)


if __name__ == '__main__':
    play_games()
