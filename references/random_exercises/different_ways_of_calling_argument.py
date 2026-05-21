# different ways of calling an argument
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

# a Dog Named "harry"
describe_pet("harry")
describe_pet(pet_name="harry")

# a horse Named "king"
describe_pet("king", "horse")
describe_pet(pet_name="king", animal_type="horse")
describe_pet(animal_type="horse", pet_name="king")

# describe_pet(pet_name="king", "horse") wrong way
# always use positional argument first than keyword