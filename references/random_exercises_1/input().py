message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# for writing long prompt
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
# += means Concatenation this is the process of joining two or more strings together

name = input(prompt)
print(f"\nHello, {name}!")


# using int() function to accept numerical inputs.
age = input("enter your age:  ")
age = int(age)