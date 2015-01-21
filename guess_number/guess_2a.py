''' Reverse guessing game: the computer guesses your number

Instead of you guessing a number randomly chosen by the computer,
have the computer ask you to enter a number first,
and implement a strategy for the computer to "guess" your number.

The program should output its guesses asking you if they are too high or
too low until a correct guess is done.
'''


def main():
    low = 1
    high = 100

    print("Think of a number between {} and {}".format(low, high))

    print("When you are ready,"
          " let me know and I will attempt to guess your number.")
    input("\nEnter anything and I will start: ")

    def valid_input():
        while True:
            reply = input("\nEnter 'low', 'high' or 'correct'.   ")
            if reply in ('low', 'high', 'correct'):
                return reply
            print("I do not understand what you wrote.")

    while True:
        guess = (low + high)//2
        print("I am guessing {}".format(guess))
        reply = valid_input()
        if reply == 'low':
            low = guess
        elif reply == 'high':
            high = guess
        else:
            print("Thank you for playing with me!")
            break

        if low == high:
            print("You cheated!")
            break

if __name__ == '__main__':
    main()
