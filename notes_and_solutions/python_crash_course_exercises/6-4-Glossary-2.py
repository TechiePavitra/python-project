# Now that you know how to loop through a dictionary, 
# clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls 
# with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

# Dictionary from 6-3 
glossary = {
    "variable": "a name that stores a value",
    "string": "text data wrapped in quotes",
    "list": "an ordered collection of items",
    "dictionary": "a collection of key-value pairs",
    "function": "a reusable block of code that does a specific task",
    "set": "an unordered collection of unique elements",
    "snippet": "a small reusable piece of code",
    "loop": "repeats code multiple times",
    "key": "the unique name used to access a value in a dictionary",
    "tuple": "an ordered collection that cannot be changed",
}

# for Loop
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning.capitalize()}")