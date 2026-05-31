# Using a program you wrote that has one function in it, 
# store that function in a separate file.
# Import the function into your main program file, 
# and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# 1st Approach
import number_generator
number_generator.value_generator(1, 10, "even")
print() # blank line

# 2nd Approach
from modules.number_generator import value_generator
value_generator(1, 10, "odd")
print() # blank line

# 3rd Approach
from modules.number_generator import value_generator as vg
vg(1, 5, "even")
print() # blank line

# 4th Approach
import number_generator as nm
nm.value_generator(1, 11, "odd")
print() # blank line

# 5th Approach
from modules.number_generator import *
value_generator(1, 11, "odd")
print() # blank line