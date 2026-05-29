# use this if the module is stored in same folder
# this is filename
import make_pizza
# use this if the module is stored in different folder
# here with first used filename and than function name
from modules.make_pizza import make_pizza

# now we can call function
make_pizza(15, "extra cheese", "pepproni")