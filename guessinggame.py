# Ben and Sam
# 11/4/19
# Guessing game where you select the difficulty and try and guess the number as
# the program tells you if you are too high or low
import random

def max_num_select():
    answer = int(input("Please enter the level of difficulty you would like to play.\nPress 1 to play on Easy.\nPress 2 to play on Medium.\nPress 3 to play on Hard."))
    if answer == 1:
        max_number = 100
        print("It's between 1 and 100")
    elif answer == 2:
        max_number = 500
        print("It's between 1 and 500")
    elif answer == 3:
        max_number = 1000
        print("It's between 1 and 1000")
    return max_number


# Select the randomized number


def number_selection():
    max_number = max_num_select()
    pick_the_number = random.randint(1,max_number)
    guess_number(pick_the_number,max_number)

# allows user to guess the number

def guess_number(pick_the_number,max_number):
    user_selection = 0
    user_guesses = [0]
    while user_selection != pick_the_number:
        user_selection = int(input("Enter a number between 1 and " + str(max_number) + ":"))
        user_guesses.append(1)
        if user_selection == pick_the_number:
            print("You win.")
            print("It took you " + str(sum(user_guesses)) + " attempts to guess the number correctly.")
        elif user_selection < pick_the_number:
            print("The number is higher.")
        elif user_selection > pick_the_number:
            print("The number is lower.")
    answer = int(input("Do you want to play again? (Enter 1 to play again or 2 to exit)"))
    if answer == 1:
        number_selection()
    elif answer == 2:
        exit()

def __init__():
    number_selection()

__init__()

