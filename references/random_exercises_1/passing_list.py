def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print(f"\nHello, {name.title()}!")
        print("Welcome to this program!")
    
users = ["michael", "john", "steve", "alex"]
greet_user(users)