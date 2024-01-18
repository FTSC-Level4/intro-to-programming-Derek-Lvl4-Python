#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code

#near the beginning of your program to print a message saying the deli has run out of pastrami, 
#and then use a while loop to remove all 

#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders = ["tuna", "ham and cheese", "pastrami", "turkey club", "vegetarian", "pastrami", "BLT", "pastrami"]

# I made an empty list for finished sandwiches
finished_sandwiches = []

print("Sorry, we have run out of pastrami.")

# Remove all of 'pastrami' from sandwich_orders using a while loop
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Loop through each sandwich order
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order from the list

   
    print(f"I made your {current_order} sandwich.")

    # Add the finished sandwich to the list
    finished_sandwiches.append(current_order)

# Print a message for each finished sandwich
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())