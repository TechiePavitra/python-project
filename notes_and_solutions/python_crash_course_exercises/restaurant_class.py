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