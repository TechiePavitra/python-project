# Arbitary allow us to call a function with unlimited arguments,
# and after collecting it, it packs it into a tuple,
# this is very helpful, when you don't have a fixed of perameters,

def build_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

build_pizza('extra cheese')
build_pizza('extra cheese', 'pepproni', 'green peppers')
# now look without any errors the 2nd function call also works
# The asterisk in the parameter name *toppings tells Python to make a tuple called toppings,
# containing all the values this function receives.
# The print() call in the function body produces output showing that Python can 
# handle a function call with one value and a call with three values.
# It treats the different calls similarly.
# Note that Python packs the arguments into a tuple, 
# even if the function receives only one .