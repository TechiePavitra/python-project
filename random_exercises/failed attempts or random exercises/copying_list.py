names = ['michael', 'rahul', 'deep', 'rohit', 'mohit']
copy_names = names[:]
copy_names.append('dinesh')
names.append('hitesh')
print("Here are the names:")
for name in names:
    print(name.title())
print()
print("Here are the copy names:")
for copy_name in copy_names:
    print(copy_name.title())


numbers = list(range(1, 101))
even_numbers = numbers[1:101:2] # Even Numbers
odd_numbers = numbers[0:101:2] # Odd Numbers
print(f"Even Numbers are {even_numbers}")
print() # Blank Space
print(f"Odd Numbers are {odd_numbers}")


