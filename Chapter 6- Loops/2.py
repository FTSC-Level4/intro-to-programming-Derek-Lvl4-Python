
# 'while true' can create an inifinite loop that can continue until the user exit it.
# The 'ValueError' will propmt if the user enter an invalid number.


while True:
    # Get user's age
    age_str = input("Enter your age (type 'exit' to end): ")

    # Check if the user wants to exit the loop
    if age_str.lower() == 'exit':
        break

    try:
        # Convert age input to an integer
        age = int(age_str)

        # Calculate ticket cost based on age
        if age < 3:
            ticket_cost = 0
        elif 3 <= age <= 12:
            ticket_cost = 10
        else:
            ticket_cost = 15

        # Display the ticket cost
        print(f"The cost of your movie ticket is ${ticket_cost}")
    
    except ValueError:
        print("Invalid input. Please enter a valid age or 'exit'.")