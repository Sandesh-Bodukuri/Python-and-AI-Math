import numpy as np

# A standard 1D vector
x = np.array([10, 20, 30])
print(f"Original shape: {x.shape}")  # (3,)

# 1. Adding Dimensions with np.newaxis (or None)
# Convert to a 2D column vector -> shape (3, 1)
col_vec = x[:, np.newaxis]
print(f"Column vector shape: {col_vec.shape}")
print(col_vec)
# Output:
# [[10]
#  [20]
#  [30]]

# Convert to a 2D row vector -> shape (1, 3)
row_vec = x[np.newaxis, :]  # Or: x[None, :]
print(f"Row vector shape: {row_vec.shape}")

# 2. Removing Dummy Dimensions with np.squeeze()
# A 3D tensor with redundant singleton dimensions: (1, 3, 1)
tensor = np.array([[[10], [20], [30]]])
print(f"\n3D Tensor shape: {tensor.shape}")  # (1, 3, 1)

# Squeeze strips away all axes of size 1 -> flattens to (3,)
squeezed = np.squeeze(tensor)
print(f"Squeezed shape: {squeezed.shape}")  # (3,)
print("Squeezed values:", squeezed)
