# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
my_ticket = [1, 2, 'A', 'D']

winning_ticket = []
count = 0

while winning_ticket != my_ticket:
    winning_ticket = []      
    
    index = 1
    while index <= 4:
        winning_ticket.append(choice(lottery_numbers))
        index += 1

    count += 1

print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {count} tries to win.")