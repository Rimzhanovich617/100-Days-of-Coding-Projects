import os
import random

## Introduction to the guessing game
## The computer will randomly generate a number between 1 and 100
## There are two modes: Easy and Hard
## Easy mode allows the user 10 tries to guess the computers choosen number
## Hard mode allows the user 5 tries to guess the computers choosen number
print("Welcome to the Number Guessing Game!")
print("You will get either 5 or 10 chances to guess a number 1 to 100.")
print("You can play on either easy or hard.")
print("Easy mode you'll get 10 guesses.")
print("Hard mode you'll get 5 guesses.")
print("Which mode would you like to choose, type either easy or hard.")

## Users guess. It will be lowercased
user_mode = input().lower()

## Defining Easy Mode and the set of instructions that'll run for 10 guesses
def easy_mode():
    print("You've chosen easy mode! You get 10 attempts to guess a number between 1 to 100.")
    print("Let's begin!")
    print("What number is your first guess? ")
    user_guess = int(input()) ## not a floating integer
    numbers_list = []
    for i in range(1, 101):
        numbers_list.append(i)
    random_choice = random.choice(numbers_list)
    computers_guess = random_choice

    attempts = 10 ## number of attempts for the user to get

    while user_guess != computers_guess: ## loop will begin counting down from 10

        if user_guess > 100 or user_guess < 1:
            print("That number is not in range.")

        if user_guess < computers_guess:
            print(f"Your guess is {user_guess}, that is too low. You have {attempts} left. Guess again.")
            user_guess = int(input())

        elif user_guess > computers_guess:
            print(f"Your guess is {user_guess}, that is too high.  You have {attempts} left. Guess again.")
            user_guess = int(input())
        else:
            print("That's not quite right. Try again.")

        attempts = attempts - 1 ## reset the count -1 per guess
        if attempts == 0:
            print("You're out of guesses! Thanks for playing.")
            quit()

    if user_guess == computers_guess:
        print(f"Your guess is {user_guess}. That is correct, You win!!!")
        print("Thank you for playing!")
        quit()


## Defining Hard Mode and the set of instructions for the user
def hard_mode():
    print("You've chosen hard mode! You get 5 attempts to guess a number between 1 to 100.")
    print("Let's begin!")
    print("What number is your first guess? ")
    user_guess = int(input()) ##not a float, negative integer, 0, or larger than 100
    numbers_list = []
    for i in range(1, 101):
        numbers_list.append(i)
    random_choice = random.choice(numbers_list)
    computers_guess = random_choice

    attempts = 5 ## number of attempts for the user to guess

    while user_guess != computers_guess:

        if user_guess > 100 or user_guess < 1:
            print("That number is not in range.")

        if user_guess < computers_guess:
            print(f"Your guess is {user_guess}, that is too low. You have {attempts} left. Guess again.")
            user_guess = int(input())

        elif user_guess > computers_guess:
            print(f"Your guess is {user_guess}, that is too high.  You have {attempts} left. Guess again.")
            user_guess = int(input())

        attempts = attempts - 1 ## count for number of guesses deducted by 1
        if attempts == 0:
            print("You're out of guesses! Thanks for playing.")
            quit()

    if user_guess == computers_guess:
        print(f"Your guess is {user_guess}. That is correct, You win!!!")
        print("Thank you for playing!")
        quit()


## Run Easy Mode if user chooses easy in the above script
if user_mode == "easy":
    easy_mode()

## Run Hard Mode if user chooses hard in the above script
elif user_mode == "hard":
    hard_mode()

## Quit program if the user doesn't guess appropriately
else:
    print("That's not a response. Thanks for playing!")
    quit()
