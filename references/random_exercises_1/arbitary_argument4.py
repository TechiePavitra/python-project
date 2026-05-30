def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert',  'einstein', location="princeton", field="physics")
print(user_profile)

# Now the first two arguments are required,
# now the **user_info acts as dictionary,
# we can add information to it,
# we use keyword arbitary to store name-value pair information
# with this special name **kwargs 
# The function will work no matter how many additional key-value pairs are provided in the function call.