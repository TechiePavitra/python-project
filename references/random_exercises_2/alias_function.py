from modules.pizza import make_pizza as mp
mp(16, "extra cheese", "pepproni")

# Now we are going to store all our modules in modules folder,
# look at the syntax:
# from folder_name.module_name import function_name as mp

# here we used "as" keyword to give nickname or alias to function
# The as keyword renames a function using the alias you provide
# The import statement shown here renames the function make_pizza() to mp() in this program