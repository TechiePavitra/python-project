aliens = []

for alien_number in range(30):
    alien_data = {
        "color": "green",
        "points": 5,
        "speed": "medium",
    }
    aliens.append(alien_data)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "red"
        alien["points"] = 10
        alien["speed"] = "slow"
        
    elif alien["color"] == "yellow":
        alien["color"] = "blue"
        alien["points"]  = 15
        alien["speed"] = "fast"

for alien in aliens[:10]:
    print(alien)

print("...")