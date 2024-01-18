#Start with the list you used in Exercise 1, but instead of just

#printing each person’s name, print a message to them. The text of each message should be the same, but each message should be 

#personalized with the person’s name.



names = ["Cyruz", "Gab", "Ricci"]

#I use the for loop statement to iterate through the names list. 
# The loop variable name represents each of my friend's name in the list, one at a time.
#I use the format method to create a message for every friend. 
# {} is the placeholder for the names

for name in names:
    message = "Hi, {}! I hope you're having a great day.".format(name)
    print(message)