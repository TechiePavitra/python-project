from random import randint, choice

a = randint(1, 10)
fruits = ['apple', 'banana', 'strawberry']
fruit = choice(fruits)

print(a, fruit)

# if you are working on a fun project, like a game, the random module is fine,
# but you need to avoid in larger and security related projects (OTP, Authentication), 
# because we can theoretically predict the number,
# use secrets module (library) for security related projects

