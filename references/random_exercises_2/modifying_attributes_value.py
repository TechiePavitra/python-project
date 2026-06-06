class Car:
    """A Simple attempt to represent car."""

    # Attributes / constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color 
        self.odometer_reading = 0 # this is default attribute
    
    # Methods
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints a statement showing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_car = Car("lamborghini", "sian", 2022, "red")

# Here are three different approaches to modify attributes value
# 1st: Through Instance
my_car.odometer_reading = 34

# Sometimes you’ll want to access attributes directly like this, 
# but other times you’ll want to write a method that updates the value for you.

# 2nd: Through 
class Car:
    """A Simple attempt to represent car."""

    # Attributes / constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color 
        self.odometer_reading = 0 # this is default attribute
    
    # Methods
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints a statement showing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_car = Car("lamborghini", "sian", 2022, "red")

# Look here we are updating odometer
my_car.update_odometer(4506)
my_car.read_odometer()