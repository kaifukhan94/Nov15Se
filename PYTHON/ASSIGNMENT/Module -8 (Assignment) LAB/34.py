# 34) Write a Python program to search for a word in a string using re.search(). 


import re

string = "Welcome to Python world"

if re.search("Python", string):
    print("Word found in string")
else:
    print("Word not found")
