# Format: [8-char ID][10-char Date][5-char Status]
raw_log = "USER_1012026-03-15SUCCESS"

user_id = raw_log[:8]         # Start to index 8
date_str = raw_log[8:18]      # Index 8 to 18
status   = raw_log[18:]       # Index 18 to end

print(f"User: {user_id}, Date: {date_str}, Status: {status}")
# Output: User: USER_101, Date: 2026-03-15, Status: SUCCESS



# 2. Window Sampling & Pagination
dataset = ["Page1", "Page2", "Page3", "Page4", "Page5", "Page6", "Page7"]

# Sample every 3rd page starting from the first
sampled = dataset[::3]
print(f"Sampled pages: {sampled}")


# Truncate to top 3 items
top_three = dataset[:3]
print(f"Top 3: {top_three}")


# 3. String Manipulation & Palindrome Checking

def is_palindrome(text: str) -> bool:
    # Clean text and compare string directly against its reverse
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")



# 4. In-Place List Mutation (Slice Assignment)
numbers = [10, 20, 30, 40, 50]

# Replace items at indices 1 to 3 directly without altering object identity
numbers[1:4] = [99, 88]
print(f"Mutated list: {numbers}")

# Wipe the list contents in-place
numbers[:] = []
print(f"Cleared list: {numbers}")
