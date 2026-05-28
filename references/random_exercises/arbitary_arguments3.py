def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    # Grammar correction
    if len(toppings) > 1:
        print(f"Making a {size}-inch pizza with the following toppings: ")
    else: 
        print(f"Making a {size}-inch pizza with the following topping: ")
    
    # Iteration through toppings
    for topping in toppings:
        print(f" -{topping.title()}")
        
make_pizza(12, "extra cheese", "pepproni")
make_pizza(16, "extra cheese")

# This syntax works no matter how many arguments the function receives.