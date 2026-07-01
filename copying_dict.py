# Original data
original_data = {
    "user": "Alice",
    "scores": [90, 85, 88]  # This list is mutable
}

# Attempting to create a "copy" (Shallow Copy)
# This creates a new dictionary, but 'scores' still points to the SAME list
copied_data = original_data.copy()

# We modify the nested list in the 'copied' version
copied_data["scores"].append(95)

# The "Implicit" part:
# We didn't touch 'original_data', but it changed anyway!
print(f"Original: {original_data['scores']}") 
print(f"Copied:   {copied_data['scores']}")

import copy

# Using deepcopy to create independent copies of nested lists
safe_copy = copy.deepcopy(original_data)

safe_copy["scores"].append(99)

print(f"Original: {original_data['scores']}") # Remains unchanged
print(f"Safe Copy: {safe_copy['scores']}")    # Has the new value