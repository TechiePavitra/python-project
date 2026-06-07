# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User:
    """Generates information about user."""
    # Attributes
    def __init__(self, first_name, last_name, region, email):
        self.first_name = first_name
        self.last_name = last_name
        self.region = region
        self.email = email
        self.login_attempts = 0
    
    # Methods
    def describe_user(self):
        print("\nUser Profile Information:  ")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Region: {self.region}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name} Welcome back! to this program")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Instances        
user_01 = User("Michael", "Jackson", "United States", "michaeljackson@outlook.com")
user_02 = User("Pranav", "Patel", "India", "pranavpatel1994@gmail.com")
user_03 = User("Sumit", "Khant", "India", "sumitkhant2008@hotmail.com")


# Calling Method
user_01.describe_user()
user_02.greet_user()
user_03.describe_user()
user_03.greet_user()

# Checking Increment Login attempts increment and rest Login attempts
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()

# Checking Incrementation
print(f"\nTotal Login Attempts: {user_01.login_attempts}")

# Resetting Login Attempts
user_01.reset_login_attempts()
print(f"Total Login Attempts: {user_01.login_attempts}")