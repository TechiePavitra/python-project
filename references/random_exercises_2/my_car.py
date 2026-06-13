# Import modules
from modules.car import Car, ElectricCar

# Base Car
my_new_car = Car("audi", "a4", 2024) # Creating an Instance
print(my_new_car.get_descriptive_name()) # Getting descriptive Name
my_new_car.odometer_reading = 25 # Accessing Attribute
my_new_car.read_odometer() # Reading Odometer

# ElectricCar Class
tesla = ElectricCar("tesla", "model 4", 2024)
print(f"\n{tesla.get_descriptive_name()}")
tesla.update_odometer(1205)
tesla.read_odometer()
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()