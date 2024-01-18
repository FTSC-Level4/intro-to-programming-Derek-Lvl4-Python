

# Create a list of people you'd like to invite to dinner
guests = ["Cyruz Baguio", "Gab Valenciano", "Ricci Rivero"]

# Use a for loop to send dinner invitations
#I use the format method to create a message for the invitation of every guest. 
#The name of the guest is included in the message that is kept in the invitation variable.

for guest in guests:
    invitation = "Dear {}, you are invited to dinner at my place.".format(guest)
    print(invitation)