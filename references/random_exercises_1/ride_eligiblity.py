# less pythonic code
height = input("How tall are you?, in inches:  ")
height = int(height)

if height >= 48:
    print(f"\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# more pythonic code
height = int(input("How tall are you?, in inches:  "))

if height >= 48:
    print(f"\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")