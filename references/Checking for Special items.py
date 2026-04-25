#  Normal requested toppings list of restaurant
requested_toppings = ["extra cheese", "green peppers", "mushrooms"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping.title()}!")

print("\n Finished Making your Pizza!")

# what if the restaurant runs out of green peppers?
requested_toppings = ["extra cheese", "green peppers", "mushrooms"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry!, We are out of green peppers right now")
    else:
        print(f"adding {requested_topping}")

print("We finished making your pizza!")

# Practice Problem
# Imagine you've a Grocery Store
# You have a list of items a customer wants to buy:
# apples, milk, bread, eggs, butter
# the bread is out of stock today
# check every item and print msg according to from django.conf import settings

shopping_list = ["apples","bread","eggs","butter", "milk"]

for shopping_list_item in shopping_list:
    if shopping_list_item == "bread":
        print("Sorry, bread is out of stock today.")
    else:
        print(f"Adding {shopping_list_item.title()} to your cart.")

print("\nYour Shopping is done!")

# this code checks wether a customer needs plain pizza or with toppings (addons)
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# one thing about this code, you need to remember that a empty list means
# false, python checks an empty list as false, so here the first statement so if is false
# so else get's printed out
# look what happens when the list has at least one topping
requested_toppings = ['red peppers']
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")  

# Here we check if the requested toppings in available toppings or not
available_toppings = ["extra cheese", "green peppers", "mushrooms"]
requested_toppings = ['extra cheese', 'french fries', 'mushrooms']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"{requested_topping.title()} are available")
    else:
        print(f"{requested_topping.title()} are unavailable")
     

# Imagine you've a library a customer orders bulk of books with their titles
# you need to check you've the available stock or not
# make a available_books list and than requested_books
# check that requested_books are available or not   
# make a list of unavailable books
available_books = ["harry potter", "rich dad poor dad", "atomic habits", "thinking, fast and slow"]
requested_books = ["harry potter", "the alchemist", "atomic habits"]
unavailable_books = ["python crash course"]

for requested_book in requested_books:
    if requested_book in available_books:
        print(f"The Book: {requested_book.title()} is available")
    else:
        print(f"The Book: {requested_book.title()} is unavailable")
        unavailable_books.append(requested_book)
        
for unavailable_book in unavailable_books:
    print(f"The {unavailable_book.title()} is temporarily unavailable! it'll be available soon!")