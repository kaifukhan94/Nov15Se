# 5) Write a Python program to open a file in write mode, write some text, and then close it. 


# Open file in write mode
file = open("sample.txt", "w")

# Write text into the file
file.write("Hello, this is a sample text file.\n")
file.write("This file is created using Python.")

# Close the file
file.close()

print("Data written to file successfully.")