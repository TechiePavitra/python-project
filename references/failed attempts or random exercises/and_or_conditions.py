# deepesh said: Kya dono bhaiyo mai se koi 18+ hai? Answer me yes or not

deep = 16
deep_jr = 20

# 0 P Q PVQ
# 1 T T T
# 2 T F T
# 3 F T T - This condition applies in this situation. 
# 4 F F F
    
    # false          # true = true
if (deep >= 18) or (deep_jr >= 18):
    print("Yes, dono bhaiyo mai se koi ek 18+ hai") # for true print this / this applies for the situation.
else:
    print("No, Dono mai se ek bhi 18+ nahi hai") # for false print this.


username = input("Enter Your Username:  ")
username_db = ['yug', 'mohit', 'dinesh', 'michael', 'mohan']

if username.lower() in username_db:
    print("This username has been already in our database!")
else:
    print("This username is available! and now has been added..")
    username_db.append(username.lower())

print(username_db)


# Imagine mojang is giving free vanilla capes to users who are 2 years old in Minecraft, and also owns Both Editions Java & Bedrock
owns_both_edition = True
year = 5

# Checking Eligiblity
if (owns_both_edition) and (year >= 2):
    print("You are Eligible to Get The Vanilla Cape!")
else: 
    print("You are not Eligible to Get The Vanilla Cape!")
    
    
    
# Set n True For Even Numbers.
# Set n False For Odd Numbers.
# New Update Added custom way to set limits
even, odd = True, False
n = odd
lim = 100     # limit

# Set
set_num = []

# if-else statement
if n:
    for i in range(2, lim+1, 2): # Even Numbers
        set_num.append(i)
else: 
    for i in range(1, lim+1, 2): # Odd Numbers
        set_num.append(i)
        
# Display Numbers for Testing
for i in set_num:
    print(i)
        
