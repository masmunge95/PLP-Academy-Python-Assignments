def calculator():
    print("🎉 Welcome to my simple Calculator! 🎉")
    print("You can add, subtract, multiply, or divide two numbers.")
    print("Type 'q' anytime to quit.\n")

    while True:
        # Step 1: Ask for the first number OR quit
        num1_input = input("Enter the first number (or 'q' to quit): ")
        if num1_input.lower() == "q":
            print("👋 Thanks for using the Fun Calculator! Goodbye!")
            break
        try:
            num1 = float(num1_input)
        except ValueError:
            print("❌ That is not a valid number! Try again.\n")
            continue

        # Step 2: Ask for the second number
        num2_input = input("Enter the second number: ")
        try:
            num2 = float(num2_input)
        except ValueError:
            print("❌ That is not a valid number! Try again.\n")
            continue

        # Step 3: Ask for the arithmetic operator to be used
        operator = input("Enter the arithmetic operator (+, -, *, /): ")

        # Step 4: Perform the right operation for the operator used
        if operator == "+":
            result = num1 + num2
            print(f" ✅ {num1} + {num2} = {result}\n")
        elif operator == "-":
            result = num1 - num2
            print(f" ✅ {num1} - {num2} = {result}\n")
        elif operator == "*":
            result = num1 * num2
            print(f" ✅ {num1} × {num2} = {result}\n")
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
                print(f" ✅ {num1} ÷ {num2} = {result}\n")
            else:
                print("🚨 Error: You cannot divide a number by zero!\n")
        else:
            print("⚠️ Invalid operator! Please use +, -, *, or /.\n")

# Run the calculator
calculator()
# This is a simple calculator program that performs basic arithmetic operations.