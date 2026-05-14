# Start with the program you wrote for Exercise 6-1 (page 98). 
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through
# the list, print everything you know about each person.

# People
michael = {
    "first_name": "michael",
    "last_name": "jackson",
    "age": 50, # when he died
    "city": "los angeles", 
}

john = {
    "first_name": "john",
    "last_name": "thompson",
    "age": 21, 
    "city": "las vegas", 
}

steve = {
    "first_name": "steve",
    "last_name": "smith",
    "age": 21, 
    "city": "new york", 
}

# List
people = [michael, john, steve]

# For Loop
for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} Information:")
    print(f"\tFirst Name: {person['first_name'].title()}")
    print(f"\tLast Name: {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")



    
    
    