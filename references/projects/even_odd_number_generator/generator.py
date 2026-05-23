# Change Variable "even"
# if you want Even Numbers use "even = True"
# if you want Odd Numbers use "even = False"
even_numbers = []
odd_numbers = []

num = 1 
limit = 100 # change this variable to manuplate this program.

while num <= limit:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    num += 1

print("Here are even numbers: ")
for even_number in even_numbers:
    print(even_number)

print("\nHere are odd numbers: ")
for odd_number in odd_numbers:
    print(odd_number)        