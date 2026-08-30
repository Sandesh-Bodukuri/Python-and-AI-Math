import numpy as np

# Sample dataset with out-of-range sensor readings
readings = np.array([-15, 2, 45, 88, 120, 5, -3])

# 1. Basic Value Clamping: np.clip(array, min_val, max_val)
# Force all values to stay strictly within [0, 100]
clamped = np.clip(readings, a_min=0, a_max=100)

print("Original readings:", readings)
print("Clamped readings: ", clamped)

# 2. Clamping Only One Side (Upper or Lower Bound Only)
# Set negative values to 0, leaving higher values untouched
positive_only = np.clip(readings, a_min=0, a_max=None)
print("Positive only:   ", positive_only)

# 3. In-Place Clamping (Zero Memory Allocation)
pixel_data = np.array([240, 260, 150, -10, 300])

# Mutates pixel_data directly via the 'out' parameter
np.clip(pixel_data, 0, 255, out=pixel_data)
print("In-place pixels: ", pixel_data)