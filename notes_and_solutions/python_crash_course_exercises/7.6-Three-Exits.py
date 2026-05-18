# Write different versions of either Exercise 7-4 or 7-5 
# that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' 

# Version 1: conditional test
prompt = "\nPlease enter a pizza topping"
prompt += "\n(Enter 'quit' when done):  "

requested_toppings = []
message = ""

while message.lower() != 'quit':
    message = input(prompt)
    
    if message.lower() != 'quit':  
        requested_toppings.append(message.lower())
        print(f"{message} will be added to your pizza!")

print("\nHere is list of your requested toppings:")
for topping in requested_toppings:
    print(topping.title())
    

# Version 2: while active 
prompt = "\nPlease enter a pizza topping"
prompt += "\n(Enter 'quit' when done):  "

requested_toppings = []
active = True

while active:
    message = input(prompt)
    
    if message.lower() == 'quit':
        active = False
    else:
        requested_toppings.append(message.lower())
        print(f"{message} will be added to your pizza!")

print("\nHere is list of your requested toppings:")
for topping in requested_toppings:
    print(topping.title())
    
# version 3: while True + break 
prompt = "\nPlease enter a pizza topping"
prompt += "\n(Enter 'quit' when done):  "

requested_toppings = []

while True:
    message = input(prompt)
    
    if message.lower() == 'quit':
        break
    else:
        requested_toppings.append(message.lower())
        print(f"{message} will be added to your pizza!")

print("\nHere is list of your requested toppings:")
for topping in requested_toppings:
    print(topping.title())