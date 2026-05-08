# Change Variable "even"
# if you want Even Numbers use "even = True"
# if you want Odd Numbers use "even = False"

even = True
lim = 100 # Adjust Limit Here
numbers = [] # Use This list Later, when you need to use

# Loop
if even:
    for even_number in range(2, lim + 1, 2):
        numbers.append(even_number)
else:
    for odd_number in range(1, lim + 1, 2):
        numbers.append(odd_number)

# Displaying Numbers
for number in numbers:
    print(number)