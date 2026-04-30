# 8) Write a Python program to write multiple strings into a file. 

# List of strings
lines = [
    "This is the first line.\n",
    "This is the second line.\n",
    "This is the third line.\n"
]

# Open file in write mode and write multiple strings
with open("multi.txt", "w") as file:
    file.writelines(lines)

print("Multiple strings written to file successfully.")