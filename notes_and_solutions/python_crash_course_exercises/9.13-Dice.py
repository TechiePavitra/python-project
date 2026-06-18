# Make a class Die with one attribute called sides,
# which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. 
# Roll each die 10 times.
import random

class Die:
    """A attempt to simulate dice."""
    
    # Attributes
    def __init__(self, sides=6):
        self.sides = sides
    
    # Methods
    def roll_die(self):
        number = random.randint(1, self.sides)
        print(number)

# Instances
six_dice = Die()
ten_dice = Die(10)
twenty_dice = Die(20) 

# 6-sided die
print("\n6-sided die:  ")
for i in range(10):
    six_dice.roll_die()

# 10-sided die
print("\n10-sided die:  ")
for i in range(10):
    ten_dice.roll_die()

# 20-sided die
print("\n20-sided die:  ")
for i in range(10):
    twenty_dice.roll_die()
