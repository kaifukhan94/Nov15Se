# 12) Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 


# try:
#     # Taking input from user
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     op = input("Enter operator (+, -, *, /): ")

#     # Performing calculation
#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "/":
#         result = num1 / num2   # May raise ZeroDivisionError
#     else:
#         print("Invalid operator!")
#         result = None

#     # Display result if valid
#     if result is not None:
#         print(f"Result = {result}")

# # Handle division by zero
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# # Handle invalid input (e.g., letters instead of numbers)
# except ValueError:
#     print("Error: Invalid input! Please enter numeric values.")



try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")
