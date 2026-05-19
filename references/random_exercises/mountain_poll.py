# make an empty dictionary
responses = {}
polling_active = True # flag

# while loop
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
             
             # key    # value
    responses[name] = response # added key & value to dictionary
    
    # if user enters 'no' than program exits 
    repeat = input("Would you like to let another person respond (yes or no):  ")
    
    if repeat.lower() == 'no':
        polling_active = False

# check if the key and value is added to dictionary or not
print(responses)