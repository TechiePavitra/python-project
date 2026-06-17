# This module is specifically made using exercise 9.12

from user import User
from privileges import Privileges
"""A Simple Admin Module"""
class Admin(User):
    """A special type of user."""
    
    # Attributes
    def __init__(self, first_name, last_name, region, email):
        super().__init__(first_name, last_name, region, email)
        self.privileges = Privileges() 