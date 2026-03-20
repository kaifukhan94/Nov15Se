# Write a Python program that manipulates and prints strings using various string methods.


text = "  python programming  "

print(len(text))                     # 1. len()
print(text.lower())                  # 2. lower()
print(text.casefold())               # 3. casefold()
print(text.upper())                  # 4. upper()
print(text.title())                  # 5. title()
print(text.capitalize())             # 6. capitalize()
print(text.strip())                  # 7. strip()
print(text.replace("python","Java",1)) # 8. replace(old,new,count)
print(text.find("pro"))              # 9. find()
print(text.startswith("  python"))   # 10. startswith()
print(text.endswith("  "))           # 11. endswith()

words = text.split()                 # 12. split()
print(words)

print("-".join(words))               # 13. join()

print("Python".isalpha())            # 14. isalpha()
print("12345".isdigit())             # 15. isdigit()
print("Python123".isalnum())         # 16. isalnum()

print("7".zfill(3))                  # 17. zfill()
print("Python".center(20))           # 18. center()