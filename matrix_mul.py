import numpy as np

# 1. 1D Dot Product (Vector Inner Product)

weights = np.array([0.5, 0.3, 0.2])
inputs  = np.array([10.0, 20.0, 30.0])

linear_output = weights @ inputs  # Equivalent to np.dot(weights, inputs)

print("Dot Product Output:", linear_output)
# Output: Dot Product Output: 17.0

# 2. 2D Matrix Multiplication (@ operator)
# Matrix A: Shape (2, 3) -> 2 samples, 3 features
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Matrix B: Shape (3, 2) -> 3 input weights, 2 output classes
B = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

# Standard multiplication `A * B` fails here because shapes don't match for element-wise math.
# Matrix Multiplication: (2, 3) @ (3, 2) -> Results in shape (2, 2)
result_matrix = A @ B

print("Matrix Product (A @ B):\n", result_matrix)

# 3. Transposing with .T for Shape Alignment
# If matrices are (2, 3) and (2, 3), flip dimensions of the second matrix:
C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[7, 8, 9], [1, 2, 3]])

# C @ D -> Dimension mismatch error
# C @ D.T -> (2, 3) @ (3, 2) -> Valid!
aligned_product = C @ D.T
print("\nAligned with Transpose (C @ D.T):\n", aligned_product)