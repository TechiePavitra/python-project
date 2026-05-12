# USER-DATABASE
users = {
    "aeinstein": {
        "fname": "albert",
        "lname": "einstein",
        "location": "princeton",
    },
    
    "mcurie": {
        "fname": "marie",
        "lname": "curie",
        "location": "paris",
    },
}

# FOR LOOP
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['fname']} {user_info['lname']}"
    location = user_info['location']
    
    # FULL NAME & LOCATION
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")