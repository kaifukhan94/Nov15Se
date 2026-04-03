# 21) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.  



# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "marks": 85,
    "city": "Delhi"
}

# Extracting keys and values
keys = student.keys()
values = student.values()

# Display keys and values
print("Keys:", list(keys))
print("Values:", list(values))