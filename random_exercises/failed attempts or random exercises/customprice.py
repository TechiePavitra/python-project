# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("adding mushrooms")
    
# elif 'extra cheese' in requested_toppings:
#     print("adding extra cheese")

## cloned
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
    
del requested_toppings[1]   
    
requested_toppings.insert(-1, 'extra cheese')
if 'extra cheese' in requested_toppings:
    print("adding extra cheese")
    