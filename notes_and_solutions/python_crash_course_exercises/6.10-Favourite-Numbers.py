# Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favourite_numbers = {
    "mohit": [1],
    "rohit": [3, 7, 5],
    "sumit": [7, 4, 8],
    "ganesh": [1, 7, 9],
    "hiren": [6, 2, 3],
}

for name, numbers in favourite_numbers.items():
    
    if len(numbers) > 1:
        print(f"{name.title()}'s Favourite Numbers are given below:")
        
        for number in numbers:
            print(f"\t{number}")
    
    else:
        for number in numbers:
            print(f"{name.title()}'s Favourite Numbers is {number}")