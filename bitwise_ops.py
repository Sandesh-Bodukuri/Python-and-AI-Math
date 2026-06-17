# Standard Python integers
a = 12  # Binary: 1100
b = 5   # Binary: 0101

print(f"Binary of {a}: {bin(a)}")
print(f"Binary of {b}: {bin(b)}")
print("-" * 30)

# 1. Bitwise AND (&)
# 1100 & 0101 = 0100 (4)
result_and = a & b
print(f"{a} & {b} = {result_and} (Binary: {bin(result_and)})")

# 2. Bitwise OR (|)
# 1100 | 0101 = 1101 (13)
result_or = a | b
print(f"{a} | {b} = {result_or} (Binary: {bin(result_or)})")

# 3. Bitwise XOR (^)
# 1100 ^ 0101 = 1001 (9)
result_xor = a ^ b
print(f"{a} ^ {b} = {result_xor} (Binary: {bin(result_xor)})")

# 4. Bitwise NOT (~)
# Inverts bits. In Python, integers are signed (Two's Complement).
# ~12 = -(12 + 1) = -13
result_not = ~a
print(f"~{a} = {result_not}")

# 5. Left Shift (<<)
# Shifts bits of 12 (1100) left by 1: 11000 (24)
result_left = a << 1
print(f"{a} << 1 = {result_left} (Binary: {bin(result_left)})")

# 6. Right Shift (>>)
# Shifts bits of 12 (1100) right by 1: 110 (6)
result_right = a >> 1
print(f"{a} >> 1 = {result_right} (Binary: {bin(result_right)})")

print("-" * 30)
print("Bitwise operations with NumPy arrays:")

import numpy as np

# Create two arrays
arr1 = np.array([12, 10, 5])
arr2 = np.array([5, 3, 6])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")

# Perform element-wise bitwise operations
print(f"AND: {np.bitwise_and(arr1, arr2)}")
print(f"OR:  {np.bitwise_or(arr1, arr2)}")
print(f"XOR: {np.bitwise_xor(arr1, arr2)}")
print(f"Left Shift: {np.left_shift(arr1, 1)}")
print(f"Right Shift: {np.right_shift(arr1, 1)}")