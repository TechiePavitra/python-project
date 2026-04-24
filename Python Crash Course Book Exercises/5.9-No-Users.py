# Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

# My answer / My Code:
users = []

if users:
    for user in users:
        if user == "admin":
            print(f"Hello {user.title()}, would you like to see a status report?") # .title() method is extra
        else:
            print(f"Hello {user.title()}, thank you for logging") # .title() method is extra
else:
    print("We need to find some users!")



