# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll.

# Empty dictionary and flag
dream_vacation = {}
active = True

# While Loop
while active:
    # User data entry
    name = input("Please Enter your Name:  ")
    prompt = "If you could visit one place in the world,"
    prompt += "\nwhere would you go?:  "
    destination = input(prompt)
    dream_vacation[name] = destination
    
    # to exit the program
    question = input("would you like to let another person enter (yes or no):  ")
    if question == 'no':
        active = False
        
# Poll Results
print("\n--- Poll Results ---")
for name, destination in dream_vacation.items():
    print(f"{name}'s dream place to visit is {destination}")