# Make a class called User. 
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() 
# that prints a personalized greeting to the user.
# Create several instances representing different users, 
# and call both methods for each user.

class User:
    """Generates information about user."""
    # Attributes
    def __init__(self, first_name, last_name, region, email):
        self.first_name = first_name
        self.last_name = last_name
        self.region = region
        self.email = email
    
    # Methods
    def describe_user(self):
        print("\nUser Profile Information:  ")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Region: {self.region}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name} Welcome back! to this program")

# Instances        
user_01 = User("Michael", "Jackson", "United States", "michaeljackson@outlook.com")
user_02 = User("Pranav", "Patel", "India", "pranavpatel1994@gmail.com")
user_03 = User("Sumit", "Khant", "India", "sumitkhant2008@hotmail.com")


# Calling Method
user_01.describe_user()
user_02.greet_user()
user_03.describe_user()
user_03.greet_user()