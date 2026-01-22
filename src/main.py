import random
import time

def welcome():

    print("\n\n\n\n\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")
    

def select_difficulty():

    print("\nPlease select the difficulty level:")
    print("\t1. Easy (10 chances)")
    print("\t2. Medium (5 chances)")
    print("\t3. Hard (3 chances)")

    dif = int(input("\nEnter your choice: "))

    while dif not in [1, 2, 3]:
        dif = int(input(("Please enter a valid difficulty level: ")))

    dif_extended = get_extended_difficulty(dif)

    print("\nGreat! You have selected the " + dif_extended + " difficulty level.")
    print("Let's start the game!")

    return dif

def get_extended_difficulty(dif):

    if dif == 1: return "Easy"
    elif dif == 2: return "Medium"
    else: return "Hard"

def get_number_tries(dif):

    if dif == 1: return 10
    elif dif == 2: return 5
    else: return 3

def game(dif, num):

    tries = get_number_tries(dif)
    win = False

    time_init = time.time()

    for i in range(tries):

        guess = int(input("\nEnter your guess: "))

        if guess < num: print("Incorrect! The number is greater than " + str(guess) + ".")
        elif guess > num: print("Incorrect! The number is less than " + str(guess) + ".")
        else:
            time_end = time.time()
            duration = time_end-time_init

            print("Congratulations! You guessed the correct number in " + str(i+1) + " attempts during a total of " + str(int(duration)) + " seconds.")
            win = True
            break

    if not win:
        print("\nSorry, you have run out of guesses...")
        print("The correct number was " + str(guess) + "...")
        print("\nBetter luck next time!")

if __name__ == "__main__":

    welcome()
    difficulty = select_difficulty()

    correct_number = random.randint(1, 100)
    
    game(difficulty, correct_number)