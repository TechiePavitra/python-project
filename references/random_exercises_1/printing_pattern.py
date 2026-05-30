# print this pattern using a for loop
# *
# **
# ***
# ****
# *****

for i in range(1, 7):
    print("*" * i)
    
# *
# **
# ***
# ****
# ***
# **
# *

# Upper Part
for i in range(1, 5):
    print("*" * i)

# Lower Part
# Starting from 3
for i in range(3, 0, -1):
    print("*" * i)
