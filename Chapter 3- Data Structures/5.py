# Create a list of people you'd like to invite to dinner
guests = ["Michael Jordan", "Leonardo da Vinci", "Marie Curie"]

# I Print a message stating the name of the guest who can't make it
guest_not_coming = "Marie Curie"
print("{} can't make it to dinner.".format(guest_not_coming))

# Replace the name of the guest who can't make it with a new person
new_guest = "Isaac Newton"
guests.remove(guest_not_coming)
guests.append(new_guest)

# I Use the for loop to send the updated dinner invitations
for guest in guests:
    invitation = "Dear {}, you are invited to dinner at my place.".format(guest)
    print(invitation)