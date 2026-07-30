numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# 1. Basic Slicing [start:stop]
subset = numbers[2:6]
print(f"Index 2 to 5: {subset}")

# 2. Using Step [::step]
evens_by_position = numbers[::2]  # Every second element
print(f"Every 2nd item: {evens_by_position}")


# 3. Negative Step (Reversing)
reversed_list = numbers[::-1]
print(f"Reversed: {reversed_list}")
#

# 4. Shallow Copying
copy_of_list = numbers[:]  # Creates a clean duplicate
print(f"Is copy identical object? {copy_of_list is numbers}")