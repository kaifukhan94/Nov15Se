# 7) Write a Python program to sort a list using both sort() and sorted().



my_list = [5, 2, 9, 1, 7]

# Using sort() (modifies original list)
my_list.sort()
print("List after sort():", my_list)


my_list2 = [5, 2, 9, 1, 7]

# Using sorted() (returns a new list)
new_list = sorted(my_list2)
print("List after sorted():", new_list)

# Original list remains unchanged
print("Original list:", my_list2)