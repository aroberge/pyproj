''' Modified from http://inventwithpython.com/hangman.py

* Changed names to follow PEP 8; this includes the fact that
  variable local to a function should be in all lowercase
  - strive to seek that no line is longer than 80 characters
* Extracted common part of images into separate string
* Used prompt argument for input() instead of separate print()
* Changed some comments into proper docstrings
* Used set comparison instead of looping over letters in word.
* Added new function spaced_print to avoid repeating code
* Used string.format method to print
* Used list comprehension to build underscored word as in "_ a n _ _ a n"
* Used str.isalpha() to avoid typing the entire alphabet
* Moved "if game_is_done" to top of loop and introduced boolean to avoid
  repeating code

'''

import random

COMMON_PIC = '''

  +---+
  |   |{}
      |
=========

'''

HANGMAN_PICS = ['''
      |
      |
      |''', '''
  O   |
      |
      |''', '''
  O   |
  |   |
      |''', '''
  O   |
 /|   |
      |''', '''
  O   |
 /|\  |
      |''', '''
  O   |
 /|\  |
 /    |''', '''
  O   |
 /|\  |
 / \  |''']

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
 crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard
 llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python
 rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider
 stork swan tiger toad trout turkey turtle weasel whale wolf wombat
 zebra'''.split()


def get_random_word(wordList):
    '''This function returns a random string from the passed list of strings.'''
    world_index = random.randint(0, len(wordList) - 1)
    return wordList[world_index]


def spaced_print(word):
    '''Print a word, with one space between letters, adding a new line
     at the end'''
    for letter in word:
        print(letter, end=' ')
    print()


def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    '''displays the board after each guess, showing the progress on the
       hangman picture, the letters guessed so far, both correct and
       incorrect.
    '''
    print(COMMON_PIC.format(hangman_pics[len(missed_letters)]))
    print('Missed letters:', end=' ')
    spaced_print(missed_letters)
    blanks = [letter if letter in correct_letters else '_'
              for letter in secret_word]
    spaced_print(''.join(blanks))


def get_guess(already_guessed):
    ''' Returns the letter the player entered.
        This function makes sure the player entered a single letter,
        and not something else.
    '''
    while True:
        guess = input('Guess a letter.\n').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    ''' This function returns True if the player wants to play again,
        otherwise it returns False.
    '''
    return input('Do you want to play again? (yes or no)\n'
                ).lower().startswith('y')


# ==== End of definitions =============

print('H A N G M A N')
first_time = True

while True:
    if first_time or game_is_done:
        if first_time or play_again():
            first_time = False
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break

    display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess
        found_all_letters = set(secret_word) == set(correct_letters)
        if found_all_letters:
            print('Yes! The secret word is "{}"! You have won!'.format(
                                                                   secret_word))
            game_is_done = True
    else:
        missed_letters = missed_letters + guess
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(HANGMAN_PICS, missed_letters, correct_letters,
                          secret_word)
            print('You have run out of guesses!\n After', end=' ')
            print('{} missed guesses'.format(len(missed_letters)), end=' ')
            print('and {} correct guesses'.format(len(correct_letters)), end='')
            print(', the word was "{}".'.format(secret_word))
            game_is_done = True

