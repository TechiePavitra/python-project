# use this if the module is stored in same folder
# this is filename
import pizza
# use this if the module is stored in different folder
# here with first used filename and than function name
from modules.pizza import make_pizza

# now we can call function
pizza.make_pizza(15, "extra cheese", "pepproni")

# for method second
make_pizza(15, "extra cheese", "pepproni")