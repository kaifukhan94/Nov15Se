# 6) Write a Python program to create a file and write a string into it.


# Create a file and write a string into it
with open("output.txt", "w") as file:
    file.write("This is a sample string written to the file.")

print("File created and data written successfully.")