#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
#Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "\t   Derek Macalagay\n"

# Print the name with whitespace
print("Name with whitespace:")
print(name)

# Print the name using stripping functions
print("\nStripped Names:")
print("Using lstrip():", name.lstrip())
print("Using rstrip():", name.rstrip())
print("Using strip():", name.strip())