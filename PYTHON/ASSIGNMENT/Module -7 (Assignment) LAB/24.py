# 24) Write a Python program to create a calculator using functions.


# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +  -  *  /")
choice = input("Enter choice: ")

# Performing calculation
if choice == "+":
    print("Result:", add(num1, num2))
elif choice == "-":
    print("Result:", subtract(num1, num2))
elif choice == "*":
    print("Result:", multiply(num1, num2))
elif choice == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")








# # Function definitions
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# # Taking input
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Choose operation: +  -  *  /")
# choice = input("Enter choice: ")

# # Using match-case (switch)
# match choice:
#     case "+":
#         print("Result:", add(num1, num2))
#     case "-":
#         print("Result:", subtract(num1, num2))
#     case "*":
#         print("Result:", multiply(num1, num2))
#     case "/":
#         print("Result:", divide(num1, num2))
#     case _:
#         print("Invalid choice")
