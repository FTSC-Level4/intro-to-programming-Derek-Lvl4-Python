
#The make_shirt function is defined with two parameters: size and message. 
# Medium is assigned to the 'size' parameter while Hellow world is assigned to message.


def make_shirt(size, message):
    """Prints a sentence summarizing the shirt details."""
    print(f"Shirt size: {size}, Message: {message}")

# Call the function using positional arguments
make_shirt("Medium", "Vlone")

# Call the function using keyword arguments
make_shirt(size="Large", message="Stussy")