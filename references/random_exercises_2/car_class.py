class Car:
    """A Simple attempt to represent car."""
   
    # Constructor (self) with Attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
    
    # Methods
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())