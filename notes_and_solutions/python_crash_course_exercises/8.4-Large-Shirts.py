# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(shirt_size="large", shirt_message="I love Python"):
    """Make a T-Shirt"""
    print(f"A {shirt_size}-sized shirt with the custom message '{shirt_message}' will be printed.")
    
make_shirt()
make_shirt(shirt_size="medium")
make_shirt(shirt_size="short", shirt_message="I love Programming")