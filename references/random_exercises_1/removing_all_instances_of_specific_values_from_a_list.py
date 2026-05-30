pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# what is happening here?
# the while loop is first checking that 'cat' string is in pets list or not
# if yes than this line is executing pets.remove('cat')
# means remove first element that has value of 'cat'
# what is happening here? -> check 'cat' is in lists or not 
# remove first element of that value -> repeat, until the condition
# 'cat' in pets returns false because there is no cat, the loop stops