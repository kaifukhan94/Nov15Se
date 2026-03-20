# Write a Python program to check if a number is prime using if_else.

num = int(input("Enter a number: "))
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if num <= 1:
    print("Not a prime number")
elif flag == 0:
    print("Prime number")
else:
    print("Not a prime number")