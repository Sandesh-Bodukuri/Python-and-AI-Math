import numpy as np
arr = [10, 20, 30, 40, 50]

# Access by index - O(1)
first_item = arr[0]   
last_item = arr[-1]   
print(first_item)
print(last_item)

# Append to end - O(1)
arr.append(60)
# arr is now [10, 20, 30, 40, 50, 60]

# Insert at specific index (index, value) - O(n)
arr.insert(1, 15)
# arr is now [10, 15, 20, 30, 40, 50, 60]
print(arr)
# Extend / concatenate with another array - O(k)
arr.extend([70, 80])
# arr is now [10, 15, 20, 30, 40, 50, 60, 70, 80]
print(arr)
# Remove & return last element - O(1)
last_val = arr.pop()  # Returns 80
print(arr)
# Remove & return element at specific index - O(n)
second_val = arr.pop(1)  # Removes index 1 (value 15)
print(arr)
# Remove by value (removes first matching occurrence) - O(n)
arr.remove(30)
print(arr)
# Delete by index using 'del' keyword - O(n)
del arr[0]  # Removes element at index 0
print(arr)