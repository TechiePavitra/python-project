# Module-level Docstring
"""A Set of Classes used to represent gas and electric car."""


# Parent Class 
class Car:
    """A Simple attempt to represent car."""
   
    # Constructor (self) with Attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer = 0
    
    # Methods
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer} miles on it.")
    
    def update_odometer(self, mileage):
        """Updates odometer."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer += miles
        else: 
            print("Please increment miles in positive value, distance can't be negative!")
    
    def fill_gas_tank(self):
        """Fills the gas tank of the car."""
        print("The gas tank is filling!")


# Battery as a Seperate Part / Composition
class Battery:
    """a attempt to represent Electirc car battery."""
    
    # Attributes
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    # Methods
    def describe_battery(self):
        print(f"This car has {self.battery_size}-kwh battery.")
    
    def get_range(self):
        """Tell how many miles the car can travel on a full charge."""
        range = self.battery_size * 4
        print(f"This car can go about {range} miles on")
    
    def upgrade_battery(self):
        percent = 25
        upgrade_percent = self.battery_size
        self.battery_size = round(upgrade_percent + (upgrade_percent * percent/100))

            
# Child
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