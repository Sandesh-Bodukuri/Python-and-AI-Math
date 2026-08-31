import numpy as np

# 1. 1D Array Usage
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])
temperatures = np.array([28.5, 34.2, 31.0, 39.8, 26.1])

# Find the index of the highest temperature
hottest_idx = np.argmax(temperatures)
coldest_idx = np.argmin(temperatures)

print(f"Hottest day: {days[hottest_idx]} ({temperatures[hottest_idx]}°C)")
print(f"Coldest day: {days[coldest_idx]} ({temperatures[coldest_idx]}°C)")

# 2. 2D Array Usage across an Axis
# Model prediction probabilities for 3 samples across 4 classes [Cat, Dog, Bird, Fish]
probabilities = np.array([
    [0.10, 0.75, 0.05, 0.10],  # Sample 0 -> Dog (index 1)
    [0.05, 0.10, 0.80, 0.05],  # Sample 1 -> Bird (index 2)
    [0.90, 0.02, 0.05, 0.03],  # Sample 2 -> Cat (index 0)
])

classes = np.array(["Cat", "Dog", "Bird", "Fish"])

# Find the predicted class index for each row (axis=1)
predicted_indices = np.argmax(probabilities, axis=1)

print("\nPredicted Class Indices:", predicted_indices)
print("Predicted Labels:", classes[predicted_indices])