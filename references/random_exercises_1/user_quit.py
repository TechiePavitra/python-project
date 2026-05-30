prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
    
    # message != 'quit': This is a direct comparison. 
    # It checks if message is not equal to 'quit'. 
    # not (message == 'quit'): This first checks if message is equal to 'quit' and then negates that result.
    # think it as it checks first the that it is true or false, than it makes answer opposite
    # if its true than false
    # and if its false than true
    # it's Follow's this truth table
    # P ~P
    # T F
    # F T
    # message != 'quit' is very direct 

# quit word fix
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != "quit":
    message = input(prompt)
    
    if message != "quit":
        print(message)
        
# using flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True # Flag

while active:
    message = input(prompt)
    
    if message.lower() == 'quit':
        active = False # if user enters quit than make it false
    else:
        print(message) 