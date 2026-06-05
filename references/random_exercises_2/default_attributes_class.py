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

# Why we used default attribute? and what it does?
# First look, some inputs are not possible that a user can provide,
# Like how much total distance a car travelled in its lifetime,
# We use odometer to represent a car travelled total this distance,
# By default when we buy a car the odometer is 0, because its has not travelled to any where yet,
# In this situation we need to an default attribute to store car's odometer value,
# Look at the upper code we have provided an default value, and than created a new method called read_odometer,
# Which prints "How much miles does car travelled",
# Not many cars are sold with exactly 0 miles on the odometer, 
# so we need a way to change the value of this attribute.

# Let's Create a Instance
my_car = Car("lamborghini", "sian", 2022, "red")

# Let's call method
print(my_car.get_descriptive_name())
my_car.read_odometer()