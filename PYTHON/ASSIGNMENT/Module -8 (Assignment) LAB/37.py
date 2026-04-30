# 37) Write a Python program to match a word in a string using re.match().

import re

string = "Python programming"

if re.match("Python", string):
    print("Word matched at start")
else:
    print("No match at start")
