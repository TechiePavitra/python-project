# Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business

class Restaurant:
    """Generate Information about a Restaurant."""
    
    # Attributes
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    # Methods
    def describe_restaurant(self):
        """Describes Restaurant details."""
        print(f"Restaurant Name is {self.restaurant_name}")
        print(f"Restaurant Cuisine Type is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Indicates that restaurant is open or not"""
        print(f"{self.restaurant_name} is Open")
    
    def set_number_served(self, updated_served_numbers):
        """Updates number of served customers"""
        self.number_served = updated_served_numbers
        
    def increment_number_served(self, increment):
        """Increments number of served customers"""
        if increment >= 0:
            self.number_served += increment
        else:
            print("Please use a positive number to increment number of served customers!")
        
        
restaurant = Restaurant("Tulsi Restaurant", "Indian and Chinese")

# Printing two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Added a empty print line to differ betweenn attributes and methods in output
print()

# Calling both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Current Served Customers
print(f"\nTotal Served Customers: {restaurant.number_served}")
# Updated Served Customers
restaurant.set_number_served(120)
print(f"Total Served Customers: {restaurant.number_served}")

# Increment number of customers served
restaurant.increment_number_served(45)
print(f"Total Served Customers: {restaurant.number_served}")