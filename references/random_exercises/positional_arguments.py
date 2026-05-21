def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet("dog", "riche")
describe_pet("cat","harry")

# be careful when calling an argument.
# when you mess up with it's position.
# results are funny.

describe_pet("riche", "dog")
# look here we first used dog's name and animal type.
# the results are unexpected.