alien_0 = {"color": "green"}
# to show a specific value associated with a dictionary
# first enter the dictionary name than use Square Brackets ["color"]
print(alien_0["color"]) 

# you can have unlimited pairs of key
# you can access either key
# here there are two keys "color" and "points" you can access either
alien_1 = {"color": "yellow", "points": 20}
print(alien_1["color"])
print(alien_1["points"])

# If a player shoots down this alien, 
# you can look up how many points they should 
# earn using code like this:
alien_02 = {"color": "red", "points": "5"}
new_points = alien_02["points"]
print(f"You have just earned {new_points} Points!")

# now supported but not good for large scale projects
# don't use it for collabrative projects
alien_02 = {"color": "red", "points": "5"}
print(f"You have just earned {alien_02["points"]} Points!")