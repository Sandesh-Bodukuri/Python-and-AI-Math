import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Shape:", arr.shape)   
print("Dimensions:", arr.ndim)
print("Data type:", arr.dtype)
print("Total elements:", arr.size) 


#arithmetic operations with arrays
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)       
print("Multiplication:", a * b) 
print("Scalar Math:", a * 2)    
print("Exponent:", a ** 2)      