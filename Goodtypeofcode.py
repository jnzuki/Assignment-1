# Calculator Program - Following the correct practices.

# Addition
def add(x, y):
    return x + y

#  Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division that includes error handling
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Main function that displays the menu and handles user input
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Taking input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if the user input is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice, please try again.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # Executing the appropriate function
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")

# Run the calculator
calculator()
