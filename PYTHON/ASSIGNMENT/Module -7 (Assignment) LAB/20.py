# 20) Write a Python program to merge two lists into one dictionary using a loop.


# Two lists
keys = ["name", "age", "marks"]
values = ["John", 20, 85]

# Creating an empty dictionary
student = {}

# Merging lists into dictionary using a loop
for i in range(len(keys)):
    student[keys[i]] = values[i]

# Display the resulting dictionary
print("Merged dictionary:", student)









