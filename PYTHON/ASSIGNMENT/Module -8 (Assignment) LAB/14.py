# 14) Write a Python program to handle exceptions in a calculator.


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Division:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")


# try:
#     # Taking input
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     operator = input("Enter operator (+, -, *, /): ")

#     # Calculator logic
#     if operator == "+":
#         print(f"Result = {num1 + num2}")
#     elif operator == "-":
#         print(f"Result = {num1 - num2}")
#     elif operator == "*":
#         print(f"Result = {num1 * num2}")
#     elif operator == "/":
#         print(f"Result = {num1 / num2}")  # may cause ZeroDivisionError
#     else:
#         print("Error: Invalid operator!")

# # Handle division by zero
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# # Handle invalid numeric input
# except ValueError:
#     print("Error: Please enter valid numbers!")

# # Handle any other unexpected errors
# except Exception as e:
#     print("Unexpected error:", e)

# finally:
#     print("Calculator program ended.")