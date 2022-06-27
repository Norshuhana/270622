#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.betavariate(0, 1, 0, 9)
    print(x)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("You Cheated!")
        else:
                print("yeah!")
        

main() 