# 16) Write a Python program to handle file exceptions and use the finally block for closing the file. 


try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist")

finally:
    try:
        file.close()
        print("File closed successfully")
    except:
        print("File was not opened")
