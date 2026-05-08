# You can add new key-value pairs anytime
# You can update it like here

alien_0 = {"color": "green", "points": 5} 
print(alien_0) 
# old output: {"color": "green", "points": 5}

# imagine we have added coordinates of alien
alien_0['x_position'] = 0 # top left area of screen
alien_0['y_position'] = 25 # 25 bottom to 0

print(alien_0) 
# new output: {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
