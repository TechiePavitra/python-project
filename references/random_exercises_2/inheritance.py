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
        print(f"This car has {self.odometer_reading} miles on it.")
    
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
        self.battery_size = 40
    
    # Methods    
    def describe_battery(self):
        print(f"This car has {self.battery_size}--kwh battery.")
    
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!") # override example!
            
# Instances
car = ElectricCar("Tesla", "Model 3", 2024)

# calling methods
car.describe_battery()
car.fill_gas_tank()