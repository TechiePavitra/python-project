# without get() method you'll see an error traceback
alien_01 = {
    "color": "yellow"
}

print(alien_01["points"])

# key doesn't exist
alien_01 = {
    "color": "yellow"
}

new_point = alien_01.get("points", "just remainder key doesn't exists")
print(f"{new_point}: Here the key doesn't exist, that's why this message is showing")

# key exists
alien_02 = {
    "color": "yellow",
    "points": 1000,
}

new_point = alien_02.get("points", "just remainder key doesn't exists")
print(f"{new_point}: Here the key exists so the value is showing here")


# get() method usage real life example
person = {
    # name  # voting id
    "rahul": 6454215457
}

print(f"The voter id is: {person.get('rahul', 'please vote first to get voter id')}")