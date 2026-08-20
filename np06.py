import numpy as np

# ---------------------------------------------------------------------
# 1. Combining Arrays (Stacking)
# ---------------------------------------------------------------------

# Sample feature sets (2 samples, 2 features each)
batch_a = np.array([[10, 20], 
                    [30, 40]])

batch_b = np.array([[50, 60], 
                    [70, 80]])

# Vertical Stack (np.vstack): Appends rows (adds new samples) -> shape (4, 2)
combined_rows = np.vstack((batch_a, batch_b))
print("Vertical Stack (Row-wise):\n", combined_rows)

# Horizontal Stack (np.hstack): Appends columns (adds new features) -> shape (2, 4)
combined_cols = np.hstack((batch_a, batch_b))
print("\nHorizontal Stack (Column-wise):\n", combined_cols)


# ---------------------------------------------------------------------
# 2. Breaking Arrays Apart (Splitting)
# ---------------------------------------------------------------------

data_matrix = np.arange(16).reshape(4, 4)
print("\nOriginal 4x4 Matrix:\n", data_matrix)

# np.vsplit(): Split into 2 equal sub-arrays along rows (e.g., Train/Test split)
train_set, test_set = np.vsplit(data_matrix, 2)
print("\nTrain Set (Top 2 rows):\n", train_set)
print("Test Set (Bottom 2 rows):\n", test_set)

# np.hsplit(): Split into 2 equal sub-arrays along columns (e.g., Features vs Target)
features, target = np.hsplit(data_matrix, 2)
print("\nFeatures (Left 2 cols):\n", features)
print("Target (Right 2 cols):\n", target)
