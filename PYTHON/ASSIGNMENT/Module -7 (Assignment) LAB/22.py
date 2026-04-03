# 22) Write a Python program to count how many times each character appears in a string.


# Input string
text = "hello world"

# Creating an empty dictionary to store counts
count = {}

# Iterating over each character in the string
for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

# Display the character counts
print("Character counts:", count)