# 13) Write a Python program to demonstrate handling multiple exceptions. 


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Invalid number entered")

except ZeroDivisionError:
    print("Division by zero is not allowed")

except Exception as e:
    print("Some other error:", e)
