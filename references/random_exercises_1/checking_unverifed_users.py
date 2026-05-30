unconfirmed_users = ["john", "michael", "candace"]
confirmed_users = []

# remember that python treats a non empty list as True
# when we move every elements to other list, the list becomes empty
# unconfirmed_users list becomes false and while loop stops!
# This is called "truthiness" in Python. 
# The loop keeps running as long as the list has items, 
# and stops automatically when the list becomes empty.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# remember we need an extra variable for pop method to store values
# when we don't write anything inside the pop() method, pop starts
# it's default behavior, it removes list last element
# like here it removes last element first, which is candace, list shrink and now michael become last element it got removed
# this happens till all items are not removed
