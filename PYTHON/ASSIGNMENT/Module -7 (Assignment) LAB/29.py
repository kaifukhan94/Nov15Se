# 29) Write a Python program to generate random numbers using the random module. 



import random

# Generate a random float between 0 and 1
print("Random float:", random.random())

# Generate a random integer between 1 and 10
print("Random integer:", random.randint(1, 10))

# Select a random element from a list
numbers = [10, 20, 30, 40]
print("Random choice:", random.choice(numbers))