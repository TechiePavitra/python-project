pizza = {
    "crust": "thick",
    "toppings": ["extra cheese", "mushroom", "pepperoni"],
}

# a customer orders a pizza in pizzaria,
# the pizza crust is thick, along with toppings
# such as extra cheese, mushroom and pepperoni

# Summarize the order
print(f"You Ordered {pizza['crust']}-crust pizza " "with following toppings:")

# note here we wrote 2 strings,
# when we wrote 2 strings or more in print, print will joint strings
# means print("abc" "abc") = print("abcabc")

for topping in pizza["toppings"]:
    print(topping.title())