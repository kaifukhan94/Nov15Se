# 29) Write a Python program to show method overloading. 


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print("Sum of 2 numbers:", obj.add(10, 20))
print("Sum of 3 numbers:", obj.add(10, 20, 30))


