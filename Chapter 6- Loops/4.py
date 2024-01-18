
#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
#Then make an empty list called finished_sandwiches.

#Loop through the list of sandwich orders and print a message for each order, 
#such as I made your tuna sandwich. As each sandwich is made, 

#move it to the list of finished sandwiches. After all the sandwiches have been made, 
#print a message listing each sandwich that was made.


# Make a list of sandwich orders
sandwiches = ["tuna", "ham and cheese", "turkey club", "vegetarian", "BLT"]

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Loop through each sandwich order
while sandwiches:
    current_order = sandwiches.pop(0)  

#pop(0) is used to take the first order from the list of sandwich orders.
    
    # Display a message for each order
    print(f"I made your {current_order} sandwich.")

    # Add the finished sandwich to the list
    finished_sandwiches.append(current_order)

# Print a message for each finished sandwich
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)