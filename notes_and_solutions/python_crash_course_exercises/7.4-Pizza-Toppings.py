# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
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