import numpy as np
one_dimensional_array = np.array([10,12])
print(one_dimensional_array)
k = np.array([[4,8,7],[5,6,9]])
print(k)
#Get Dimension
print(one_dimensional_array.ndim)

#Get Shape
print(k.shape)

# 1D Array
np_array_1d = np.array([10, 20, 30, 40], dtype=np.int32)

# 2D Matrix initialized with zeros
np_zeros_2d = np.zeros((2, 3), dtype=np.float64)

# Multiplied instantly via vectorization without loops
scaled_array = np_array_1d * 2

print("NumPy 1D:", np_array_1d)
print("NumPy 2D Zeros:\n", np_zeros_2d)
print("Scaled NumPy:", scaled_array)