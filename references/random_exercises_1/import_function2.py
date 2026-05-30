# Importing an entire module
# syntax:
# import module_name
# module_name.function_name
import pizza
pizza.make_pizza(16, "extra cheese", "pepproni")

# To import specific function from module
# syntax:
# from module_name import function_name

from pizza import make_pizza
make_pizza(12, "extra cheese", "pepproni")

# you can import as many functions as you want,
# using this syntax:
# from module_name import function_0, function_1, function_2

# for this program it is more better to use 2nd synax:
from pizza import make_pizza
make_pizza(12, "extra cheese", "pepproni")
# because the module have only one function