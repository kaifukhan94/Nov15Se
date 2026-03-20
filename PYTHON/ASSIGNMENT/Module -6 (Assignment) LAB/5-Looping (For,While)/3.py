# Write a Python program to find a specific string in the list using a simple for loop and if condition. 


# List of fruits
List1 = ['apple', 'banana', 'mango']

# String to search
search = input("Enter fruit to search: ")

# Using for loop and if condition
for fruit in List1:
    if fruit == search:
        print("Fruit found in the list")
        break
else:
    print("Fruit not found in the list")