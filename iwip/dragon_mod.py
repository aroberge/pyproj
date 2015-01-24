'''Modified from http://inventwithpython.com/dragon.py

* Changed intro function into multiline string
* Used prompt argument for input() instead of separate print()
* Added docstrings
* Removed empty print(), replacing by newline character
* Changed function and variable names to follow PEP8
* Replaced
    var != str1 and/or var != str2
  by
    var [not] in (str1, str2)
'''

import random
import time

INTRO = '''
You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.

'''

def choose_cave():
    '''Give the user the choice of one of two caves.
       Return the chosen value as a string'''
    cave = ''
    while cave not in ('1', '2'):
        cave = input('Which cave will you go into? (1 or 2)')

    return cave


def check_cave(chosen_cave):
    '''Give feedback to user based on choice of cave'''
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! '
          'He opens his jaws and...\n')
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')


play_again = 'yes'
while play_again in ('yes', 'y'):

    print(INTRO)
    cave_number = choose_cave()
    check_cave(cave_number)

    play_again = input('\nDo you want to play again? (yes or no)')
