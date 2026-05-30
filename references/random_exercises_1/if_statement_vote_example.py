# Percentage
a = int(input("Enter Value of A:  "))
b = int(input("Enter Value of B:  "))

if b == 0:
    print("Undefined") # if user enters second value 0
else:
    print(f"{(a/b)*100}%") # Logic