# Basic Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

def get_number(prompt):
    """
    Function to get a valid number (integer or float) from the user.
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """
    Function to get a valid operation from the user.
    Keeps asking until a valid operation (+, -, *, /) is entered.
    """
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please choose +, -, *, or /.")

def perform_calculation(num1, num2, operation):
    """
    Function to perform the arithmetic operation.
    Handles division by zero.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

def main():
    """
    Main function to run the calculator loop.
    """
    print("Welcome to the Basic Calculator!")
    while True:
        # Get the first number
        num1 = get_number("Enter the first number: ")

        # Get the second number
        num2 = get_number("Enter the second number: ")

        # Get the operation
        operation = get_operation()

        # Perform the calculation
        try:
            result = perform_calculation(num1, num2, operation)
            print(f"The result of {num1} {operation} {num2} is: {result}")
        except ZeroDivisionError as e:
            print(e)

        # Ask if the user wants to perform another calculation
        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()