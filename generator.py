def count_up_to(max_number: int):
    """Generates numbers up to max_number one by one without creating a full list."""
    current = 1
    while current <= max_number:
        # 'yield' pauses the function and sends a value back to the caller
        yield current  
        current += 1
    # When loop finishes, the generator automatically stops

# 1. Using it directly in a for-loop
print("--- Generator Loop ---")
for num in count_up_to(3):
    print(f"Number: {num}")

# 2. Fetching values manually using next()
gen = count_up_to(2)

print(next(gen))  # Returns 1, pauses function
print(next(gen))  # Resumes, returns 2, pauses function
# Calling next(gen) again now would raise StopIteration error safely caught by loops