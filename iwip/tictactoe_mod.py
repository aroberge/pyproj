''' Tic Tac Toe modified from http://inventwithpython.com/tictactoe.py

* Change names to follow PEP 8
* Have proper docstrings for functions
* Use prompt argument of input() instead of print() followed by empty input().
* Use var not in (str1, str2)

'''
import random

board_repr = '''\
   |   |
 {7} | {8} | {9}
   |   |
-----------
   |   |
 {4} | {5} | {6}
   |   |
-----------
   |   |
 {1} | {2} | {3}
   |   |'''

def draw_board(board):
    '''Prints a board passed as a list of 10 strings, with the
       first string being ignored.
    '''

    print(board_repr.format('dummy', board[1], board[2], board[3], board[4],
                            board[5], board[6], board[7], board[8], board[9]))

def input_player_letter():
    '''Ask the player which letter they want to be;
       returns a list with the player's letter as first iem and the
       computer's letter as the second item.
    '''
    letter = ''
    while letter not in ('X', 'O'):
        letter = input('Do you want to be X or O?\n').upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():
    '''Randomly choose the player who goes first.'''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    return input('Do you want to play again?'
                 ' (yes or no)\n').lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """Given a board and a player's letter,
         this function returns True if that player has won."""
    # We use bo instead of board and le instead of letter so we don't
    # have to type as much.
    return (
    (bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def get_player_move(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choose_random_move(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if is_space_free(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def get_computer_move(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computerLetter, i)
            if is_winner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, playerLetter, i)
            if is_winner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move(board, [2, 4, 6, 8])

def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            draw_board(theBoard)
            move = get_player_move(theBoard)
            make_move(theBoard, playerLetter, move)

            if is_winner(theBoard, playerLetter):
                draw_board(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = get_computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)

            if is_winner(theBoard, computerLetter):
                draw_board(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
