# Define the menu with items and their prices
menu = {
    'A': {'name': 'Cola', 'price': 1.50},
    'B': {'name': 'Water', 'price': 1.00},
    'C': {'name': 'Snack', 'price': 2.00},
    'D': {'name': 'Juice', 'price': 2.50},
    'E': {'name': 'Chips', 'price': 1.75},
    'F': {'name': 'Chocolate', 'price': 1.80}
}

def display_menu():
    """Display the menu to the user."""
    print("Vending Machine Menu:")
    for code, item in menu.items():
        print(f"{code}: {item['name']} - ${item['price']}")

def get_user_input():
    """Capture the user's inputted code."""
    code = input("Enter the code of the item you want to purchase (or 'Q' to quit): ")
    return code.upper()

def calculate_change(total_cost, user_amount):
    """Calculate and return the change."""
    return user_amount - total_cost

def main():
    total_cost = 0

    while True:
        # Display the menu
        display_menu()

        # Get user input
        selected_code = get_user_input()

        # Check if the user wants to quit
        if selected_code == 'Q':
            break

        # Check if the selected code is valid
        if selected_code not in menu:
            print("Invalid code. Please select a valid item.")
            continue

        # Get the selected item details
        selected_item = menu[selected_code]
        item_name = selected_item['name']
        item_price = selected_item['price']

        # Get user's money input
        user_money = float(input(f"Enter the amount of money for {item_name} ($): "))

        # Calculate total cost and change
        total_cost += item_price
        change = calculate_change(total_cost, user_money)

        # Check if user has enough money
        if change < 0:
            print("Insufficient funds. Please insert more money.")
            total_cost -= item_price  # Undo the cost addition
            continue

        # Dispense the item and provide change
        print(f"Dispensing {item_name}...")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Change: ${change:.2f}")

if __name__ == "__main__":
    main()