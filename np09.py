import numpy as np

# A 2D matrix (2 rows, 3 columns)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 1. Using .flatten() -> Returns an independent copy
flat_copy = matrix.flatten()
flat_copy[0] = 999

print("Flattened copy:", flat_copy)
print("Original matrix (unchanged):")
print(matrix)

# 2. Using .ravel() -> Returns a memory-efficient view
flat_view = matrix.ravel()
flat_view[0] = 100

print("\nFlattened view:", flat_view)
print("Original matrix (modified via view):")
print(matrix)