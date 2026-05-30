prompt = "\nEnter your favourite city"
prompt += "\nor you can quit this program by entering 'quit':  "

while True:
    message = input(prompt)
    
    if message.lower() == 'quit':
        break
    else:
        print(message)

# why to use break?
# break immediately exits loops the loop
# you can use in simple programs, but in complex program
# always use flags, like in elif statement program

# break also works in a for loop and dictionary
# like if need to find certain thing, if we got that thing
# than you need to break that loop
