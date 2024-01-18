

#The favorite_book is known with a single parameter 'title'.
# I use an f string to include the 'title' parameter in the message output.


def favorite_book(title):
    """Prints a message about a favorite book."""
    print(f"One of my favorite books is {title}.")

# Call the function with a book title as an argument
favorite_book("Alice in Wonderland")