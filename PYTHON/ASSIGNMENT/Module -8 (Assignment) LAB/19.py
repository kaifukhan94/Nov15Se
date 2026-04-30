# 19) Write a Python program to create a class and access the properties of the class using an object. 


# Create a class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object
p1 = Person("Kaif", 23)

# Access class properties using object
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")