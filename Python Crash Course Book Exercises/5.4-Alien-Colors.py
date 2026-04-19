# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block

# First Version
alien_color = 'green'
if alien_color == 'green':
    points = 5
else:
    points = 10
print(f"The player just earned {points} points.")

# Second Version
alien_color = 'red'
if alien_color == 'green':
    points = 5
else:
    points = 10
print(f"The player just earned {points} points.")