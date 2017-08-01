'''
guessthenumber.py

This program lets the user play against the computer
and guess a random number between 1 and 10.
'''

import sys
import random

def guessTheNumber():
    secretNumber = random.randint(1, 10)
    guesses = []  # start with empty list

    print("Welcome to Guess the Number!\nTry to figure out what the secret number is!")

    while len(guesses) < 5:
        try:
            guess = int(input("\nGuess a number between 1 and 10: "))
        except ValueError:
            print("{} is not a number!".format(guess))
        else:
            if guess == secretNumber:
                print("You got it! My number was {}.".format(secretNumber))
                break
            elif guess in guesses:
                print("You already guessed that number!\n")
            #gives users a little hint.
            elif guess < secretNumber:
                print("My number is higher than {}.".format(guess))
            elif guess > secretNumber:
                print("My number is lower than {}.".format(guess))

            else:
                print("That's not it!")
            guesses.append(guess) #adds number to the list
    else:
        print("\nSorry, you lost. My number was {}.".format(secretNumber))

    play_again = input("Would you like to play again? Y/N: ")
    if play_again.lower() == 'y':
        guessTheNumber()
    else:
        print("Ok, bye!")
        sys.exit(0)

guessTheNumber()

sys.exit(0)
