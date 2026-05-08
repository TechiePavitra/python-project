# Be aware that the deleted key-value pair is removed permanently.
alien_01 = {"color": "green", "points": 5}
print(f"{alien_01} this is old")

# now we're removing the key value pair here,
# we need to use del statement same as we used in lists

del alien_01["points"]
print(f"{alien_01} this is updated")