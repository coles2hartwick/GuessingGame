import random

# Select the randomized number
def number_selection():
    max_number = 100
    pick_the_number = random.randint(1,max_number)
    guess_number(pick_the_number,max_number)


def guess_number(pick_the_number,max_number):
    user_selection = 0
    while user_selection != pick_the_number:
        user_selection = int(input("Enter a number between 1 and" + str(max_number)))

        if user_selection == pick_the_number:
            print("You win.")
        elif user_selection < pick_the_number:
            print("Too low guess a higher number.")
        elif user_selection > pick_the_number:
            print("Too high of a guess pick a lower number.")

number_selection()

