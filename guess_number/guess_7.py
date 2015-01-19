''' Guess the number: Full GUI using PyQt

Simple version where nothing is saved between games.
'''

import random
from PyQt4 import QtGui, QtCore

class GameWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_layout()
        self.max_nb = 100

    def create_layout(self):
        '''Creates the very simple game layout'''
        self.setWindowTitle("Guess the number game!")
        self.resize(400, 200)

        self.label = QtGui.QLabel("Your guess", self)
        self.label.move(10, 40)
        self.entry = QtGui.QLineEdit(self)
        self.entry.returnPressed.connect(self.analyze_guess)
        self.entry.move(150, 40)
        self.new_game_button = QtGui.QPushButton("New Game", self)
        self.new_game_button.clicked.connect(self.new_game)
        self.new_game_button.move(150, 80)

        self.waiting_for_game()
        self.show()

    def safe_exit(self):
        '''Mostly a placeholder when it will be time to save the
           information to a file/database, etc.

           For now, it simply shows an exit message before quitting.
        '''
        box = QtGui.QMessageBox()
        box.setWindowTitle("Goodbye!")
        box.setText("Thanks for playing!")
        box.show()
        box.raise_()
        QtCore.QTimer.singleShot(1500, self._quit)
        box.exec_()

    def _quit(self):
        '''Ends the program'''
        QtGui.qApp.quit()

    def waiting_for_game(self):
        '''Displays new game button, inviting the player to start a new game'''
        self.label.hide()
        self.entry.hide()
        self.new_game_button.show()
        self.statusBar().showMessage("Click on the button to start a new game")

    def new_game(self):
        '''Resets the relevant values and change the UI to play a game'''
        self.attempts = 0
        self.label.show()
        self.entry.setText('')
        self.statusBar().showMessage('')
        self.entry.show()
        self.new_game_button.hide()
        self.goal = random.randint(1, self.max_nb)

    def analyze_guess(self):
        '''analyze a single guess to see if the number was guessed correctly'''
        guess = self.safe_conversion(self.entry.text())
        message = ''
        if guess:
            self.attempts += 1
            if guess == self.goal:
                message = "You got it in {} attempts.".format(self.attempts)
                self.waiting_for_game()
            elif guess < self.goal:
                message = "{} is too low.".format(guess)
            else:
                message = "{} is too high.".format(guess)
            self.statusBar().showMessage(message)
        self.entry.setText('')

    def safe_conversion(self, guess):
        '''Safely converts the value entered into an integer; notifies
           the player if it can not be done.
        '''
        try:
            guess = int(self.entry.text())
            return guess
        except ValueError:
            self.statusBar().showMessage("You must enter an integer value")
            return False


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = GameWindow()
    app.aboutToQuit.connect(window.safe_exit)
    app.exec_()
