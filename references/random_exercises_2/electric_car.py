from car import Car
from battery import Battery

"""A simple class for electric car"""

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    # Attributes
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model, year)
        self.battery = Battery()
    
    # Methods        
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!") # override example!
