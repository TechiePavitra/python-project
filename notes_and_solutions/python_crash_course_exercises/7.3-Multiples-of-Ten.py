# Ask the user for a number, 
# and then report whether the number is a multiple of 10 or not.

number = int(input("Enter your number:  "))

if number % 10 == 0:
    print("This Number is Multiple of Ten.")
else:
    print("This Number is not Multiple of Ten.")