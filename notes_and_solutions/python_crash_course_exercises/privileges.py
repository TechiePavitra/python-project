# This module is specifically made using exercise 9.12
"""A Simple Privileges module."""

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