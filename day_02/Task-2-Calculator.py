"""
Interactive Calculator
"""
try:
    # To take input from user
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    # Calculations  (it will display all the four mathematical functions)
    print(f"The sum of {first_number} and {second_number} is: {first_number + second_number}")
    print(f"The difference is: {first_number - second_number}")
    print(f"The product is: {first_number * second_number}")
    print(f"The quotient is: {first_number / second_number}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
