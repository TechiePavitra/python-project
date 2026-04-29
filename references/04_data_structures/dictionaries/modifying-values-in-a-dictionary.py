# imagine as game progress the alien changes the color
# and you want to modify the key value in a dictionary
# here's how you can

alien_0 = {"color": "green"} # old
print(f"the alien color is {alien_0["color"]}") 

alien_0["color"] = "yellow" # updated the color
print(f"the alien color is now {alien_0["color"]}")

# book example:
# the alien is moving from left to right (x axis)
# if it is moving at range of slow, it'll going to move to x_position = 1
# if it is moving at range of medium, it'll going to move to x_position = 2
# if it is moving at range of fast, it'll going to move to x_position = 3

alien_1 = {
    "x_position": 0,
    "y_position": 25,
    "speed": "medium",
}
alien_1["speed"] = "fast"

print(f"Original position: {alien_1['x_position']}")

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
if alien_1["speed"] == "slow":
    x_increment = 1  
elif alien_1["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
    
# # The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment 
print(f"New position: {alien_1['x_position']}")

