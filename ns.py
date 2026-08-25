import numpy as np

# 1. 1D Fancy Indexing: Arbitrary Element Selection & Reordering

data = np.array([10, 20, 30, 40, 50, 60, 70])

# Pass a list of specific indices to extract
indices = [0, 4, 2]
extracted = data[indices]

print("Selected items:", extracted)

# Modify multiple arbitrary elements at once
data[[1, 3]] = 999
print("Mutated array:", data)
# Output: Mutated array: [ 10 999  30 999  50  60  70]


# 2. 2D Fancy Indexing: Row & Coordinate Selection

matrix = np.array([
    [10, 11, 12, 13],  # Row 0
    [20, 21, 22, 23],  # Row 1
    [30, 31, 32, 33],  # Row 2
    [40, 41, 42, 43]   # Row 3
])

# Select specific rows in a custom order (Row 3, then Row 0, then Row 1)
reordered_rows = matrix[[3, 0, 1]]
print("\nReordered Rows:\n", reordered_rows)

row_indices = [0, 2]
col_indices = [1, 3]
selected_points = matrix[row_indices, col_indices]

print("\nExtracted Coordinates:", selected_points)