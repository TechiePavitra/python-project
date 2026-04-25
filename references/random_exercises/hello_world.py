# the pythagorean theorem calculator
# Import Py Library Mathematics 
import math
a = int(input("Enter A:  "))
b = int(input("Enter B:  "))

# Logics / Formula
a_squared  = a**2
b_squared = b**2
s = a_squared + b_squared

square_root = math.sqrt(s) # Library Component
result = square_root

# Display result
print(f"if {a} and {b} are the legs of a right triangle, the hypotenuse is approximately {result}")