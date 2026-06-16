from car import Car
from electric_car import ElectricCar

tesla = ElectricCar("tesla", "model 4", 2024)
lamborghini = Car("lamborghini", "sian", 2022)

# method calls
print(tesla.get_descriptive_name())
print(lamborghini.get_descriptive_name())

# related to battery
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()