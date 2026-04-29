# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    "variable": "a name that stores a value",
    "string": "text data wrapped in quotes",
    "list": "an ordered collection of items",
    "dictionary": "a collection of key-value pairs",
    "function": "a reusable block of code that does a specific task",
}

print(f"Variable:\n\t{glossary['variable']}")
print(f"String:\n\t{glossary['string']}")
print(f"List:\n\t{glossary['list']}")
print(f"Dictionary:\n\t{glossary['dictionary']}")
print(f"Function:\n\t{glossary['function']}\n")