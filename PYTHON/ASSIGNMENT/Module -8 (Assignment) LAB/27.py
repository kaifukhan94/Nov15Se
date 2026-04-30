# 27) Write a Python program to demonstrate the use of super() in inheritance. 


class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Age:", self.age)

obj = Child("Kaif", 22)
obj.show()
obj.display()
