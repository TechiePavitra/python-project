# pizza's default size is regular in this function
def order_pizza(pizza_type, size="regular"): 
    """Ordering a pizza"""
    print(f"You are ordering a {size} sized {pizza_type.title()} pizza.")

order_pizza(pizza_type="italian") # here the default argument is "regular"
order_pizza(pizza_type="extra cheese", size="large")

# one simple rule: make the default parameter at last, 
# if not, python would get confuse, and errors can appear,

# When you use default values, 
# any parameter with a default value needs to be listed 
# after all the parameters that don’t have default values.
# This allows Python to continue interpreting positional arguments correctly.