# chapter 8 alias works same as previously in functions
from car import Car as C 
from electric_car import ElectricCar as EC

# instances 
audi = C("audi", "i8", 2017)
tesla = EC("tesla", "model 4", 2022)

print(audi.get_descriptive_name())
print(tesla.get_descriptive_name())
