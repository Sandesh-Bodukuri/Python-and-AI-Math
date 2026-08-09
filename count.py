from collections import Counter
# 1. Automatic Frequency Counting

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Dave"]

# Automatically tally frequencies into a dictionary-like object
vote_counts = Counter(votes)

print(f"Tallied Votes: {vote_counts}")
# Output: Tallied Votes: Counter({'Alice': 3, 'Bob': 2, 'Charlie': 1, 'Dave': 1})


# 2. Extracting Top Rankings (.most_common)
# Get the top N most frequent items as (item, count) tuples
top_two = vote_counts.most_common(2)

print(f"Top 2 Candidates: {top_two}")

# 3. Safe Missing Key Access & Multiset Arithmetic

# Accessing missing keys returns 0 instead of raising a KeyError
print(f"Votes for Eve: {vote_counts['Eve']}")

# Combine or subtract tallies directly using arithmetic operators
batch1 = Counter(apples=4, bananas=2)
batch2 = Counter(apples=1, bananas=5, oranges=3)

total_inventory = batch1 + batch2
print(f"Combined Inventory: {total_inventory}")
