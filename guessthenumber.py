'''
guessthenumber.py

This program lets the user play against the computer
and guess a random number between 1 and 10.
'''

import sys
import random

def guessTheNumber():
    print("Welcome to Guess the Number!")
    print("Try to figure out what the secret number is!")

    while True:
        secretNumber = random.randint(1, 10)
        guesses = set()

        while len(guesses) < 5:
            try:
                print()
                guess = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("{} is not a number!".format(guess))
            else:
                if guess in guesses:
                    print("You already guessed that number!")
                elif guess < secretNumber:
                    print("My number is higher than {}.".format(guess))
                elif guess > secretNumber:
                    print("My number is lower than {}.".format(guess))
                else:
                    print("You got it! My number was {}.".format(secretNumber))
                    print()
                    break
                guesses.add(guess)
        else:
            print()
            print("Sorry, you lost. My number was {}.".format(secretNumber))
            print()

        playAgain = input("Would you like to play again? Y/N: ")
        if playAgain.lower() == 'n':
            print("Ok, bye!")
            break

guessTheNumber()

sys.exit(0)
