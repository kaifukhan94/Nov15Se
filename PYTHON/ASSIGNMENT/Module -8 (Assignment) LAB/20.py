# 20) Write a Python program to demonstrate the use of local and global variables in a class. 



x = 100  # Global variable

class Demo:
    def show(self):
        y = 50  # Local variable
        print("Local variable:", y)
        print("Global variable inside class:", x)

obj = Demo()
obj.show()

print("Global variable outside class:", x)
