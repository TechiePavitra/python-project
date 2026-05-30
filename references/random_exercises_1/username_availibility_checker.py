# User Enters his choice here
username = input("Enter Your Username:  ")

# Existing Username or Database
existing_users = ['john', 'marie', 'michael', 'martin']

# Checking Condition
if username.lower() in existing_users:
    print("Someone else already took this username!")
else:
    print("This username is available!")