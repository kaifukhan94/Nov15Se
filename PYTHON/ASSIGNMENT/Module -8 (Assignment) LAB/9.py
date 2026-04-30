# 9) Write a Python program to create a file and print the string into the file. 

# Open file in write mode
with open("printfile.txt", "w") as file:
    print("This string is written using print() function.", file=file)

print("Data printed into file successfully.")