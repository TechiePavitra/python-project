def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a Full Name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    
print(get_formatted_name("michael", "jackson", "joseph"))
print(get_formatted_name("michael", "jackson"))
# here the middle name is in last according to positional argument,
# if you need a perfect position, you can use keyword argument, like this

print(get_formatted_name(first_name="michael", middle_name="joseph", last_name="jackson"))
# same output but less mistakes

# an empty list, string, or dictionary always returns false,
# and an if a list, string or dictionary has one element or more, it returns true.
# we can use this fact, and can use if else statement.