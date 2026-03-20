#  Write a Python program to check if a person is eligible to donate blood using a nested if.

# Input age and weight
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))

# Check eligibility using nested if
if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible to donate blood (Weight less than 50 kg)")
else:
    print("Not eligible to donate blood (Age less than 18)")