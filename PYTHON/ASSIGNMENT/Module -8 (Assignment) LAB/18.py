# 18) Write a Python program to create a class and access its properties using an object. 



# Define a class
class Student:
    # Constructor to initialize properties
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object of the class
s1 = Student("Kaif", 23)

# Access properties using the object
print("Name:", s1.name)
print("Age:", s1.age)


