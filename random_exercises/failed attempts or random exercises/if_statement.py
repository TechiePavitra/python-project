# List
cars = ['audi', 'ferrari', 'toyota', 'bmw', 'bugatti']

# Loop
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# Here is an Simple program to check the eligibliy of candidate to vote
age = int(input("Enter your Current age:  "))
if age >= 18:
    print('You are eligible to vote!')
else:
    print('You are not eligible to vote')

# User idhar password dalega, terminal use karke
password = input("Enter the Password to Enter House:  ")

# Loop / password checking
if password == 'meri billi aur mujhise meow':
    print('Aaja bhai tu aapna Bhai hai, Welcome!')
else:
    print('America kya kehta tha kya ho tum, aaj hum kehte hai tu kon hai be?!, meka laadle! Meow ghop ghop ghop...')