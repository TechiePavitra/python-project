# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize.
from random import choice

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
winning_ticket = []

index = 1
while index <= 4:
    winning_ticket.append(choice(lottery_numbers))
    index += 1

print(f"Winning ticket:\n{winning_ticket}")