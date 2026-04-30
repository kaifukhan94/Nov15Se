# 11) Write a Python program to check the current position of the file cursor using tell().


# Create and write to a file first
with open("cursor.txt", "w") as file:
    file.write("Hello Python File Handling")

# Open file in read mode
with open("cursor.txt", "r") as file:
    print("Initial cursor position:", file.tell())

    # Read some characters
    file.read(5)
    print("Cursor position after reading 5 characters:", file.tell())

    # Read more characters
    file.read(7)
    print("Cursor position after reading 7 more characters:", file.tell())