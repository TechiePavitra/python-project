# make an empty list
aliens = []

# loop for generating 30 aliens and add it into aliens list.
for alien_number in range(30):
    new_alien = {"color": "pink", "points": 5, "speed": "slow"}    
    aliens.append(new_alien)

# loop for printing alien
for alien in aliens[:5]:
    print(alien)
print("...")

# printing the length of aliens lists
print(f"There are total {len(aliens)} aliens in the list.")
