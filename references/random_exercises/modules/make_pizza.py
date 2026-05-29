def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    if len(toppings) > 1:
        print(f"\nMaking a {size}-inch pizza with the following toppings:")
    else:
        print(f"\nMaking a {size}-inch pizza with the following topping:")
    
    for topping in toppings:
        print(f" - {topping}")
        
