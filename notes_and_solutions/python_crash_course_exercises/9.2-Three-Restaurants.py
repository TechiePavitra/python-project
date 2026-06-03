# Start with your class from Exercise 9-1. 
# Create three different instances from the class,
# and call describe_restaurant() for each instance.

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

# 1st Instance / Object        
tulsi_restaurant = Restaurant("Tulsi Restaurant", "Indian and Chinese")
tulsi_restaurant.describe_restaurant()

print() # added empty print for perfect output.

# 2nd Instance / Object        
pizza_king = Restaurant("Pizza King", "Pizza and Fast Foods")
pizza_king.describe_restaurant()

print() # added empty print for perfect output.

# 3rd Instance / Object
tasty_restaurant = Restaurant("Tasty Restaurant", "French Foods")
tasty_restaurant.describe_restaurant()
