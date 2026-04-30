# 15) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 


try:
    file = open("data.txt", "r")
    a = int(input("Enter number: "))
    print(10 / a)

except FileNotFoundError:
    print("File not found")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Execution completed")




# try:
#     # Try to open a file
#     filename = input("Enter file name: ")
#     file = open(filename, "r")

#     # Read a number from file (assume first line contains a number)
#     num = int(file.readline())

#     # Take another number from user
#     divisor = int(input("Enter number to divide with: "))

#     # Perform division
#     result = num / divisor
#     print(f"Result = {result}")

#     file.close()

# # File not found exception
# except FileNotFoundError:
#     print("Error: File not found!")

# # Division by zero exception
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# # Invalid input exception
# except ValueError:
#     print("Error: Invalid input! Please enter integers only.")

# # Any other exception
# except Exception as e:
#     print("Unexpected error:", e)

# finally:
#     print("Program execution completed.")