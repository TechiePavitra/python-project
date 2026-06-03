# Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.

class Restaurant:
    """Generate Information about a Restaurant."""
    
    # Attributes
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    # Methods
    def describe_restaurant(self):
        """Describes Restaurant details."""
        print(f"Restaurant Name is {self.restaurant_name}")
        print(f"Restaurant Cuisine Type is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Indicates that restaurant is open or not"""
        print(f"{self.restaurant_name} is Open")
        
restaurant = Restaurant("Tulsi Restaurant", "Indian and Chinese")

# Printing two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Added a empty print line to differ betweenn attributes and methods in output
print()

# Calling both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
