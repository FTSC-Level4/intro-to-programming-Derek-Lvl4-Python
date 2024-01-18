#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a

#medium shirt with the default message, and a shirt of any size with a different message.
# Make a large shirt with the default message

def make_shirt(size="Large", message="I love Python"):
    """Prints a sentence summarizing the shirt details."""
    print(f"Shirt size: {size}, Message: {message}")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a custom-sized shirt with a different message
make_shirt(size="Small", message="I love Python")