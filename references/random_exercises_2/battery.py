"""A Simple Battery class"""
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
        # The Logic is different from requirement
        percent = 25
        upgrade_percent = self.battery_size
        self.battery_size = round(upgrade_percent + (upgrade_percent * percent/100))