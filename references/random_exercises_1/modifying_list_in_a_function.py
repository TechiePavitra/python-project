# Imagine you work as a Software engineer in a 3D Model company,
# and you needs to stimulate the process of making 3D Models,
# There are two functions, one makes the stimulation of printing 3D Model,
# while other that prints completed 3D model list.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    
    # This loop move the elements unprinted_designs,
    # last item to completed_models.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"{current_design} has been printed...")
        completed_models.append(current_design)
    # this first function is working like a factory,
    # takes unprinted_designs list last item and move it to completed_models list,
    # until unprinted_designs becomes empty.
    
    
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models has been printed:")
    
    # This for loop prints completed_model,
    for completed_model in completed_models:
        print(completed_model)

# List of unprinted_designs, and completed_models           
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# to make unprinted_designs list untouched you can call like this
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
# here we are using a copied list instead of using same list,
# by using this it'll won't affect on the original list and keep it

# Even though you can preserve the contents of a list by passing a copy of it to your functions, 
# you should pass the original list to functions unless you have a specific reason to pass a copy.
# It’s more efficient for a function to work with an existing list, 
# because this avoids using the time and memory needed to make a separate copy. 
# This is especially true when working with zx
# large lists.
