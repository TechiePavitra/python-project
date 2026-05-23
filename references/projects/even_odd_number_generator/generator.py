# this is a even and odd number generator function
# use "even" or "odd" in third argument to generate even or odd numbers

def number_generator(number, limit, number_type):
    """Even and odd number generator."""
    while number <= limit:
        if number_type == 'even' and number % 2 == 0:
            print(number)
        elif number_type == 'odd' and number % 2 != 0:
            print(number)
        number += 1
        
number_generator(1, 100, "odd")