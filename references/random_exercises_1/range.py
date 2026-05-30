# Python Crash Course 3rd Edtion : Try it Yourself : Chapter 4

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(1, 21):
    print(i)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

# Note: i didn't even tested this program because my computer cannot handle it
one_million = []
for i in range(1, 1_000_001):
    one_million.append(i)

for i in one_million:
    print(i)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

large_numbers = list(range(1, 1_000_001))
print(min(large_numbers)) # min function / we can also define variable for it instead of print function.
print(max(large_numbers)) # max function / we can also define variable for it instead of print function.
print(sum(large_numbers)) # sum function / we can also define variable for it instead of print function.

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = []
for value in range(1, 21, 2):
    odd_numbers.append(value)
    print(value)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
threes = []
for x in range(3, 31, 3):
    threes.append(x)
    print(x)
    
# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube
cube = []
for amount in range(1, 11):
    cubed = amount ** 3
    cube.append(cubed)
    print(cubed)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes. 
cube = [n**3 for n in range(1,11)]