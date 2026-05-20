# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as I made tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["grilled cheese sandwich", "tuna sandwich", "club sandwich", "sloopy joe sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
    
print(f"\n--- Sandwiches that were made ---")
for sandwich in finished_sandwiches:
    print(sandwich.title())