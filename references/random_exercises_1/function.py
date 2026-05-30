def greet_user():
    """Display a simple greeting.""" 
    print("Hello!")

greet_user()

# the triple string is optional, but good habit
# to write what does, this function does
# write neat and clean docstrings
# python use this for documentation

# if you slightly modify the function.
# it greet user by their username
def greet_user2(username): # username = Parameter
    """Display a simple greeting."""
    print(f"Hello {username}!")
    
greet_user2("John") # ("John") = Argument

# Argument and Parameter are two different things.
# But developers sometimes exchange it without realizing.
# there is no strict rule to memorize which is parameter or which is argument.
# you can use both anytime.