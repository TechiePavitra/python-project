# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

# Parent Class
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

# Child Class
class IceCreamStand(Restaurant):
    """Ice Cream Stand is a type of restaurant"""
    
    # Atttributes
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["vanilla", "american dry fruit", "chocolate"]
    
    # Methods
    def display_flavours(self):
        """Displays currently available flavours."""
        print("Currently Available flavours:")
        for flavour in self.flavours:
            print(f"  - {flavour.title()}")

mohan_ice_cream = IceCreamStand("Mohan Ice Cream", "Frozen Dessert")
mohan_ice_cream.display_flavours()