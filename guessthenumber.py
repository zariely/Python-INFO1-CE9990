'''
guessthenumber.py

This program lets the user play against the computer
and guess a random number between 1 and 10.
'''

import sys
import random

def guessTheNumber():
    while True:
        secretNumber = random.randint(1, 10)
        guesses = set()  # start with empty list

        print("Welcome to Guess the Number!")
        print("Try to figure out what the secret number is!")

        while len(guesses) < 5:
            try:
                print()
                guess = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("{} is not a number!".format(guess))
            else:
                if guess == secretNumber:
                    print("You got it! My number was {}.".format(secretNumber))
                    break
                if guess in guesses:
                    print("You already guessed that number!")
                    print()
                #gives users a little hint.
                elif guess < secretNumber:
                    print("My number is higher than {}.".format(guess))
                elif guess > secretNumber:
                    print("My number is lower than {}.".format(guess))

                else:
                    print("That's not it!")
                guesses.add(guess) #adds number to the list
        else:
            print()
            print("Sorry, you lost. My number was {}.".format(secretNumber))
            print()

        playAgain = input("Would you like to play again? Y/N: ")
        if playAgain.lower() == 'y':
            break #check this
        else:
            print("Ok, bye!")
            sys.exit(0)

guessTheNumber()

sys.exit(0)
