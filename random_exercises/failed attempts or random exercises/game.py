print("  _______  __   __  _______  _______  __   __  _______")
print(" |       ||  | |  ||       ||   _   ||  |_|  ||       |")
print(" |    _  ||  |_|  ||    ___||  |_|  ||       ||    ___|")
print(" |   |_| ||       ||   | __ |       ||       ||   |___ ")
print(" |    ___||_     _||   ||  ||       ||       ||    ___|")
print(" |   |      |   |  |   |_| ||   _   || ||_|| ||   |___ ")
print(" |___|      |___|  |_______||__| |__||_|   |_||_______| ")
print("            Guess the number challenge game              \n")

import random 


starting_range = int(input("Enter Your Starting Range:  "))
ending_range = int(input("Enter Your Ending Range:  "))

# random number
random_number = random.randint(starting_range, ending_range)

# loop
while True:
    number = int(input("Enter your Number:  "))
    if number < random_number:
        print("Higher")
    elif number > random_number:
        print("Lower")
    else: 
        print("You won the Game!")
        exit()
    
