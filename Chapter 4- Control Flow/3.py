
#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

#•	 If the alien is green, print a message that the player earned 5 points.
#•	 If the alien is yellow, print a message that the player earned 10 points.
#•	 If the alien is red, print a message that the player earned 15 points.
#•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.



alien_color = "green"

# Version 1
if alien_color == "green":
    points = 5
    print(f"The player earned {points} points.")
elif alien_color == "yellow":
    points = 10
    print(f"The player earned {points} points.")
else:  # Assuming the only remaining option is red
    points = 15
    print(f"The player earned {points} points.")

alien_color = "yellow"

if alien_color == "green":
    points = 5
    print(f"The player earned {points} points.")
elif alien_color == "yellow":
    points = 10
    print(f"The player earned {points} points.")
else:  # Assuming the only remaining option is red
    points = 15
    print(f"The player earned {points} points.")


alien_color = "red"

if alien_color == "green":
    points = 5
    print(f"The player earned {points} points.")
elif alien_color == "yellow":
    points = 10
    print(f"The player earned {points} points.")
else:  # Assuming the only remaining option is red
    points = 15
    print(f"The player earned {points} points.")