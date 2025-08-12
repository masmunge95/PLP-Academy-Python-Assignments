def calculate_discount():
    """
    Gets input from the user, calculates the final price after a discount,
    and prints the result.
    """
    try:
        price = float(input("Enter the retail price of the item: "))
        if price < 0:
            print("Error: Price cannot be negative.")
            return

        discount_percent = float(input("Enter the discount percentage of the item: "))
        if not (0 <= discount_percent <= 100):
            print("Error: Discount percentage must be between 0 and 100.")
            return

        # A discount is applied only if it's 20% or greater.
        if discount_percent >= 20:
            final_price = price - (price * discount_percent / 100)
        else:
            # If discount is valid but less than 20%, no discount is applied.
            final_price = price

        # Format the output to two decimal places for currency
        print(f'The final price after applying the discount is: {final_price:.2f}')
    except ValueError:
        # Catches float conversion errors
        print('Error: Please enter valid numbers for price and discount.')

def main_menu():
    """Displays the main menu and handles user interaction."""
    print("Welcome to the Discount Calculator!")

    while True:
        # Display available options
        print("\nPlease choose an option:")
        print("1. Calculate Discount")
        print("2. Quit")

        # Get user input
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            calculate_discount()
        elif choice == "2":
            print("Thank you for using the Discount Calculator!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Call the main menu function only when the script is executed directly
if __name__ == "__main__":
    main_menu()