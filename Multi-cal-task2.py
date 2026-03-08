"""multi operation calculator"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /, %, **): ")


try:
    num1 = float(num1)
    num2 = float(num2)


    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result:.2f}")

    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result:.2f}")

    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result:.2f}")

    elif operation == "/":
        
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result:.2f}")

    elif operation == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result:.2f}")

    elif operation == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result:.2f}")

    else:
        print("Error: Invalid operation selected.")


except ValueError:
    print("Error: Please enter valid numeric values.")
