names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 1. enumerate(): Loop with Index
# Syntax: enumerate(iterable, start=0)

for index, name in enumerate(names, start=1):
    print(f"Rank {index}: {name}")

# 2. zip(): Loop Multiple Sequences Simultaneously

for name, score in zip(names, scores):
    print(f"{name} scored {score} points")

# 3. Combining Both & Creating Dictionaries

# Build a dictionary directly from two lists using zip()
score_map = dict(zip(names, scores))
print(f"Score Map: {score_map}")
