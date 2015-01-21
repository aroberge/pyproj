''' Guessing game: Computer vs Computer

Design a Guesser class whose instance can guess a number,
and a Chooser class whose instance can choose randomly a number to be guessed
and indicate whether the number guessed was too high or too low.

Your program should instantiates these classes and have them
play a game using the following code:

    def main():
        guess = Guesser()
        choose = Chooser()
        from_guess = guess.guess("start")
        while True:
            result = choose.analyze(from_guess)
            from_guess = guess.guess(result)
            if from_guess is None:
                print("\n==== Game over ====")
                return

    if __name__ == '__main__':
        main()

A sample output from playing a game looks like the following:

    I am guessing 50
        Too low.
    I am guessing 75
        Too high.
    I am guessing 62
        You are correct!
    Yay!

    ==== Game over ====

'''
import random


class Guesser:
    '''Guesses an integer using a binary strategy'''
    def __init__(self):
        self.low = 1
        self.high = 100
        self.answer = (self.low + self.high)//2

    def guess(self, action):
        '''The method used to guess number, following some received feedback'''
        if action == "start":
            print("I am guessing {}".format(self.answer))
            return self.answer
        elif action == "low":
            self.low = self.answer
        elif action == "high":
            self.high = self.answer
        elif action == "correct":
            print("Yay!")
            return

        self.answer = (self.low + self.high)//2
        print("I am guessing {}".format(self.answer))
        return self.answer


class Chooser:
    '''Chooses an integer randomly and give feedback based on the number
       received'''
    def __init__(self):
        self.number = random.randint(1, 100)

    def analyze(self, guess):
        '''Method used to give feedback'''
        if guess == self.number:
            print("    You are correct!")
            return "correct"
        elif guess < self.number:
            print("    Too low.")
            return "low"
        elif guess > self.number:
            print("    Too high.")
            return "high"
        else:
            print("This should not happen!")


def main():
    guess = Guesser()
    choose = Chooser()
    from_guess = guess.guess("start")
    while True:
        result = choose.analyze(from_guess)
        from_guess = guess.guess(result)
        if from_guess is None:
            print("\n==== Game over ====")
            return

if __name__ == '__main__':
    main()
