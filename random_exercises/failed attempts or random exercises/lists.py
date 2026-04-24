# list
guest_list = ["albert einstein", "richard feynmen", "thomas edison", "nikola tesla"]

# Can't Make it code
cant_make_it = "thomas edison"
guest_list[2] = "marie curie"

# New Guests code
guest_list.insert(0, "dolly") # new guest to the beginning of my list
guest_list.insert(2, "monty") # new guest to the middle of my list
guest_list.append("rahul")  # new guest to the end of my list

# Sad News
print("Hello everyone there is a sad news, the new table i ordered was not delivered yet and it is cancelled, now only two people can come to party.")

# New Guests print
print(f"Hello, {guest_list[0].title()} there is one sit left for our dinner party, i like to invite you, thanks!")
print(f"Hello, {guest_list[2].title()} there is one sit left for our dinner party, i like to invite you, thanks!")
print(f"Hello, {guest_list[-1].title()} there is one sit left for our dinner party, i like to invite you, thanks!")

# Can't came to Party print
print(f"Dr. {cant_make_it}. cannot able to attend party due to his personal reasons.")

# Old Guests
print(f"Respected {guest_list[1].title()}. i would like to invite you for a dinner!, i appreciate your contribution in relativity")
print(f"Respected {guest_list[3].title()}. i would like to invite you for a dinner!, i appreciate your contribution in teaching and feynmen graphs.")
print(f"Respected {guest_list[4].title()}. i would like to invite you for a dinner!, i appreciate your contribution in radium and radioactivity.")
print(f"Respected {guest_list[5].title()}. i would like to invite you for a dinner!, i appreciate your contribution in electrical physics.")

# Kicked out members
kicked_guest1 = guest_list.pop(0) # used terminal to remove specific person and index numbering.
kicked_guest2 = guest_list.pop(1) # used terminal to remove specific person and index numbering.
kicked_guest3 = guest_list.pop(1) # used terminal to remove specific person and index numbering.
kicked_guest4 = guest_list.pop(1) # used terminal to remove specific person and index numbering.
kicked_guest5 = guest_list.pop(2) # used terminal to remove specific person and index numbering.

# Sorry Message to kicked out guests
print(f"Sorry Mr/Miss. {kicked_guest1.title()} you are kicked out from our party, soo sorry for that, you are kicked out due to no extra table.")
print(f"Sorry Mr/Miss. {kicked_guest2.title()} you are kicked out from our party, soo sorry for that, you are kicked out due to no extra table.")
print(f"Sorry Mr/Miss. {kicked_guest3.title()} you are kicked out from our party, soo sorry for that, you are kicked out due to no extra table.")
print(f"Sorry Mr/Miss. {kicked_guest4.title()} you are kicked out from our party, soo sorry for that, you are kicked out due to no extra table.")
print(f"Sorry Mr/Miss. {kicked_guest5.title()} you are kicked out from our party, soo sorry for that, you are kicked out due to no extra table.")

# Still Invited
print(f"Mr/Miss. {guest_list[0].title()} you are still being invited!")
print(f"Mr/Miss. {guest_list[1].title()} you are still being invited!")

# del removed peoples
del guest_list[0]
del guest_list[0]

# print after del statement
print(f"The output will be none, here is the output {guest_list} everyone is now been removed!")
