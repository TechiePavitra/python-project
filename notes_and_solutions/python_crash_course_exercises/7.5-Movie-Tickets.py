# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10; 
# and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, 
# and then tell them the cost of their movie ticket

active = True # Flag

while active:
    # user input
    age = input("Please enter your age (or 'quit' to exit): ")
    
    # valid number checker
    if age.lower() == 'quit':
        active = False
    elif int(age) < 0:
        print("Please Enter a Valid age!")
    
    # price determination
    else:
        if int(age) < 3:
            print("Your ticket is free!")
        elif int(age) < 13:
            print("You need to pay $10")
        else: 
            print("You need to pay $15")