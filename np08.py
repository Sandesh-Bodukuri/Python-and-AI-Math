import numpy as np
# 1. 2D Matrix with 1D Vector (Row Addition)
# Shape: (3, 3)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Shape: (3,) -> treated as (1, 3) during right-to-left alignment
row_add = np.array([10, 20, 30])

# Shape comparison: (3, 3) vs (1, 3) -> Compatible!
result_rows = matrix + row_add
print("Row-wise addition:\n", result_rows)

# 2. Outer Product via (N, 1) and (1, M) Broadcasting
# Shape: (3, 1) - Column vector
a = np.array([[1], [2], [3]])

# Shape: (1, 4) - Row vector
b = np.array([[10, 20, 30, 40]])

# Shape comparison: (3, 1) vs (1, 4) -> Results in (3, 4) grid
grid_product = a * b
print("\nBroadcasted Grid (3, 4):\n", grid_product)

# 3. Shape Incompatibility Example
c = np.ones((3, 2))
d = np.ones((3,))

# Shape comparison: (3, 2) vs (1, 3) -> 2 != 3 and neither is 1!
# c + d  --> Raises: ValueError: operands could not be broadcast together