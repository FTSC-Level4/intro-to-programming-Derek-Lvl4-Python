

# I use a variable name_with_whitespace to represent a person’s name with whitespace
name_with_whitespace = "\t  Derek Macalagay \n"

# Print the name once to display the whitespace around the name
print("Name:")
print(name_with_whitespace)

# Use a stripping functions to remove whitespace
# lstrip code is for left stripping
# rstrip code is for right stripping
# strip code is for both stripping
stripped_left = name_with_whitespace.lstrip()
stripped_right = name_with_whitespace.rstrip()
stripped_both = name_with_whitespace.strip()

# Print the name using each of the three stripping functions to display the code

print("Name after Left Stripping:")
print(stripped_left)

print("Name after Right Stripping:")
print(stripped_right)

print("Name after Both Stripping:")
print(stripped_both)