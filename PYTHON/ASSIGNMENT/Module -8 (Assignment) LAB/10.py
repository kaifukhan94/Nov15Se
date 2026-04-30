# 10) Write a Python program to read a file and print the data on the console. 


# Open the file in read mode
with open("printfile.txt", "r") as file:
    # Read file content
    data = file.read()

# Print the data to console
print("File Data:")
print(data)