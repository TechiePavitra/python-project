print("  _______  _______  __   __  _______")
print(" |       ||   _   ||  |_|  ||       |")
print(" |    ___||  |_|  ||       ||    ___|")
print(" |   | __ |       ||       ||   |___ ")
print(" |   ||  ||       ||       ||    ___|")
print(" |   |_| ||   _   || ||_|| ||   |___ ")
print(" |_______||__| |__||_|   |_||_______|")
print("     Guess the number challenge game              \n")

import random 

starting_range = input("Enter Your Starting Range:  ")
ending_range = input("Enter Your Ending Range:  ")

try:
    starting_range = int(starting_range)
    ending_range = int(ending_range)
    attempts = 0 # current attempts 
    active = True # Used flag instead of break for easy understanding
    random_number = random.randint(starting_range, ending_range)

    # loop
    while (attempts < 10) and active:
        # random number
        number = input(f"\nEnter your Number:  ")
        try:
            number = int(number)
            attempts += 1

            if number != random_number:
                if attempts == 10:
                    print(f"\nGame Over! The number was {random_number}")
                    active = False
                else:
                    direction = "Higher" if number < random_number else "Lower"
                    print(f"\n{10 - attempts} chances left!")
                    print(f"{direction} than {number}")
            else:
                print(f"\nYou won in {attempts} attempt(s)!")
                active = False
        except:
            print("Please enter a valid number!")
except:
    print("Please enter a valid number!")