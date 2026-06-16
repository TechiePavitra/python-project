# Using your latest Restaurant class, store it in a module. 
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, 
# and call one of Restaurant’s methods to show that the import statement is working properly.

from restaurant_class import Restaurant

tulsi_restaurant = Restaurant("Tulsi Restaurant", "Gujarati")
tulsi_restaurant.describe_restaurant()
