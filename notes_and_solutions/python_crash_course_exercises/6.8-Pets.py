# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet.

cat = {
    "name": "cat",
    "animal": "domestic",
    "owner": "mohit",
}
dog = {
    "name": "dog",
    "animal": "domestic",
    "owner": "john",
}
fish = {
    "name": "fish",
    "animal": "anamniotes",
    "owner": "steve",
}
turtle = {
    "name": "turtle",
    "animal": "reptile",
    "owner": "alex",
}

pets = [cat, dog, fish, turtle]

for pet in pets:
    print(f"{pet['name'].title()}:")
    print(f"\tAnimal Type: {pet['animal'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")
    