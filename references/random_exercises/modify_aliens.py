# first create an empty list to store alien data
aliens = []

# generate 30 aliens with same properties
for alien_number in range(30): # 0-29
    new_alien = {"color": "green", "points": 5, "speed": "medium"}
    aliens.append(new_alien)

# make the first 3 aliens different to other
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "red"
        alien["points"] = 10
        alien["speed"] = "fast"

# print first 5 aliens and see the results        
for alien in aliens[:5]:
    print(alien)
    
print("...")