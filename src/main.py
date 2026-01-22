import random
import time
import os

def clear(): os.system('clear')

def any_key():

    print("\n(press any key to continue)")
    input()

def welcome(tries, high):

    clear()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have " + str(tries) + " chances to guess the correct number.")
    if high > 0: print("\nCurrent high score: " + str(high) + " guesses")
    any_key()
    

def select_difficulty(high):

    clear()
    print("Please select the difficulty level:")
    print("\t1. Easy (10 chances)")
    print("\t2. Medium (5 chances)")
    print("\t3. Hard (3 chances)")

    print("\nIf you wish to exit the game please enter 0")

    if high > 0: print("Current high score: " + str(high) + " guesses")

    while True: # guarantees repetition

        try:
            dif = int(input("\nEnter your choice: "))

            if dif in [0, 1, 2, 3]:
                break

            print("Please enter a valid difficulty level (1, 2 or 3) or 0 to exit.")

        except ValueError: print("Please enter a valid number.")

    if dif != 0:

        clear()
        dif_extended = get_extended_difficulty(dif)
        print("\nGreat! You have selected the " + dif_extended + " difficulty level.")
        print("Let's start the game!")
        any_key()
        

    return dif

def get_extended_difficulty(dif):

    if dif == 1: return "Easy"
    elif dif == 2: return "Medium"
    else: return "Hard"

def get_number_tries(dif):

    if dif == 1: return 10
    elif dif == 2: return 5
    else: return 3

def game(dif, num, high):

    tries = get_number_tries(dif)
    win = False
    score = -1

    welcome(tries, high)

    time_init = time.time()

    for i in range(tries):

        clear()

        while True: # guarantees repetition

            try:
                guess = int(input("\nEnter your guess: "))

            except ValueError: print("Please enter a valid number.")
            else: break

        if guess < num: print("Incorrect! The number is greater than " + str(guess) + ".")
        elif guess > num: print("Incorrect! The number is less than " + str(guess) + ".")
        else:
            time_end = time.time()
            duration = time_end-time_init

            print("Congratulations! You guessed the correct number in " + str(i+1) + " attempts during a total of " + str(int(duration)) + " seconds.")
            any_key()
            win = True
            score = i+1
            break

        any_key()

    if not win:
        clear()
        print("\nSorry, you have run out of guesses...")
        print("The correct number was " + str(num) + "...")
        print("\nBetter luck next time!")
        any_key()

    return score

if __name__ == "__main__":

    high = -1
    difficulty = select_difficulty(high)

    while difficulty != 0:

        correct_number = random.randint(1, 100)
    
        score = game(difficulty, correct_number, high)

        if (score > 0 and high == -1) or (score < high and score > 0):
            high = score

        difficulty = select_difficulty(high)

    print("\nYou have decided to exit the game.\nSee you next time!\n\n")