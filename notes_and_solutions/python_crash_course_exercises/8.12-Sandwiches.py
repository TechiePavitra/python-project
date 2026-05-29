# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, 
# using a different number of arguments each time.

def make_sandwich(*items):
    """Make Sandwich with specific items"""
    if len(items) > 1:
        print("We are making your sandwich with given list of items:  ")
        for item in items:
            print(f" - {item.title()}")
    
    else: 
        print("We are making your sandwich with given list of item:  ")
        for item in items:
            print(f" - {item.title()}")

make_sandwich("cheese", "tomato", "mayo")