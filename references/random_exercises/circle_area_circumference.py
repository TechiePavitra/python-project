import math
r = float(input("Enter the radius of the Circle in Centimeters:  ")) # used float datatype for rounding decimals
# Pi value
pi = math.pi
# Formulas and logic
c = 2*pi*r # cirumference of circle
a = pi*r**2 # area of circle
d = 2*r # diameter of circle

print(f"if the radius of circle is {r} than... \n")

## Print Area
print(f"The Area of circle is {a:.2f}")
# Print Circumference
print(f"The Circumference of circle is {c:.2f}")
