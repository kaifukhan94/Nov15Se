#  Write a Python program to calculate grades based on percentage using if-else ladder. 


# Input percentage from user
percentage = float(input("Enter your percentage: "))

# Calculate grade using if-else ladder
if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
else:
    print("Fail")