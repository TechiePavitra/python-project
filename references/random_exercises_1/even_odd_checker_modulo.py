number = int(input("Enter Your Number:  "))

if number % 2 == 0:
    print(f"\nThe Number {number} is Even.")
else:
    print(f"\nThe Number {number} is Odd.")
    
# by the fact that: 
# every odd number divided by 2 remains 1 reminder.
# and every even number divided by 2 remains 0 reminder.
# the program checks if the number returns the modulo 0 than it is even
# else odd