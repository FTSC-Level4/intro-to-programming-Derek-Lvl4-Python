
#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list

#to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”






# First I created a list of car examples.
# I use the for loop to repeat through each item in the tranpotation list. 
# I used the elif method to execute multiple block of code and else statement to end the list.

favorite_transportation = ["motorcycle", "car", "bicycle", "scooter",]

for item in favorite_transportation:
    if item == "motorcycle":
        print("I would like to own a Honda motorcycle.")
    elif item == "car":
        print("I would love to have a Tesla car.")
    elif item == "bicycle":
        print("I enjoy riding a classic road bicycle.")
    elif item == "scooter":
        print("I find electric scooters convenient for short trips.")
 
