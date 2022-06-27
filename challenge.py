#!/usr/bin/env python

import random

def main():
    """Start a guessing game."""
    print("Guess the elemen!")

    elemens = [
        "lithium",
        "rubidium",
        "sodium",
        "potassium",
        "cadmium",
        "magnesium",
        "potassium"
        ]

    x = random.choice(elemens)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What elemen am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()