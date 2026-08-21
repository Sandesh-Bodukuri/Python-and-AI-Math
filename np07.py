import numpy as np

original = np.array([10, 20, 30, 40, 50])

# 1. Slicing creates a VIEW (Shared Memory)
view_slice = original[0:3]
view_slice[0] = 999  # Mutates the sliced view

print("Original after view modification:", original)

# Check if memory is shared:
print("Is it sharing memory?", view_slice.base is original)

# 2. Explicit .copy() creates an INDEPENDENT ARRAY (Safe)
safe_copy = original[0:3].copy()
safe_copy[0] = 111  # Modify only the copy
print("Safe copy:", safe_copy)
print("Original remains untouched:", original)
print("Is safe copy sharing memory?", safe_copy.base is original)
