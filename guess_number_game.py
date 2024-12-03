"""
********************************************************************************
* Project Name:  Guess Number Game
* Description:   A simple guess number game
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

import random

# Def function
def play_game():
    # Opening
    print("I'm thinking of a number between 1 and 100.")

    # Difficult
    difficulty = input("Choose difficulty: 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempt = 10
    else:
        attempt = 5
    print(f"You have {attempt} attempts remaining to guess the number.")

    # Guessing
    n = random.randint(1, 100)
    while attempt != 0:
        guess = int(input("Make a guess: "))
        if guess > n:
            attempt -= 1
            print("Too high.\nGuess again.")
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif guess < n:
            attempt -= 1
            print("Too low.\nGuess again.")
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print(f"You win! The number was {n}")
            return

    print("You've run out of guesses, you lose.")

# Main
print("Welcome to Guessing Number Game!")
play_game()
