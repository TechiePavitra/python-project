# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

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

# Child Class
class Admin(User):
    """A special type of user."""
    
    # Attributes
    def __init__(self, first_name, last_name, region, email):
        super().__init__(first_name, last_name, region, email)
        self.privileges = Privileges()       

# Composition 
class Privileges:
    """Component of Admin."""
    
    # Attributes
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
     # Methods
    def show_privileges(self):
        """Shows the privileges that a admin has."""
        print("The privileges that a admin has: ")
        for privilege in self.privileges:
            print(f" - {privilege}") 

owner = Admin("Michael", "Jackson", "America", "michaeljackson92@outlook.com")
owner.privileges.show_privileges()