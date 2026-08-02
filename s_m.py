# 1. Standard Slice Syntax: sequence[start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract even numbers (step by 2)
evens = numbers[::2]
print(f"Evens: {evens}")


# Reverse a list or string instantly using a negative step
reversed_numbers = numbers[::-1]
print(f"Reversed: {reversed_numbers}")

# 2. String Operations & Reversal

text = "Python"

# Simple string reversal
print(text[::-1])  

# Palindrome check in one line
is_palindrome = lambda s: s.lower() == s.lower()[::-1]
print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")  # Output: True


# 3. In-Place List Mutation

data = [10, 20, 30, 40, 50]

# Replace a slice in-place
data[1:4] = [99, 99]
print(f"Mutated List: {data}")