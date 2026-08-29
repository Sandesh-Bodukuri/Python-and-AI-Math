import numpy as np

# A sample array with duplicate labels or values
data = np.array(["cat", "dog", "bird", "cat", "dog", "cat"])

unique_items = np.unique(data)

print("Unique items (automatically sorted):", unique_items)

# Get Frequencies with 'return_counts=True'
items, counts = np.unique(data, return_counts=True)

for item, count in zip(items, counts):
    print(f"{item}: {count}")

# Numeric Deduplication
numbers = np.array([40, 10, 20, 10, 40, 30])
unique_nums = np.unique(numbers)

print("\nUnique numbers:", unique_nums)
# Output: Unique numbers: [10 20 30 40]