# when you don't need to worry about,
# the ordering of argument, we simply use keyword arguments.

def describe_pet(name, type):
    """Display a pet information"""
    print(f"\nMy pet name is {name.title()}")
    print(f"My pet is a {type.title()}")

describe_pet(name="rainbow", type="cow")
describe_pet(type="cow", name="rainbow")
# the following to function calls are equivalent.

# A keyword argument is a name-value pair that you pass to a function. 
# look at the output, the ordering doesn't matter now.
# we used keyword arguments.
# Keyword arguments free you from having to worry about correctly ordering your arguments in the function call.

# When you use keyword arguments, 
# be sure to use the exact names of the parameters in the function’s definition.