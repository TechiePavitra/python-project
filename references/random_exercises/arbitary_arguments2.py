def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    # Grammar correction
    if len(toppings) > 1:
        print("Making a pizza with the following toppings: ")
    else: 
        print("Making a pizza with the following topping: ")
    
    # Iteration through toppings
    for topping in toppings:
        print(f" -{topping.title()}")
        
make_pizza("extra cheese", "pepproni")
make_pizza("extra cheese")

# This syntax works no matter how many arguments the function receives.