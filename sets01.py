original_users = {"User_A", "User_B", "User_C"}

# Create a separate copy to modify safely
backup_users = original_users.copy()

# Empty out the original set
original_users.clear()

print(f"Original Set: {original_users}")  # Output: set() (This represents an empty set)
print(f"Backup Copy:  {backup_users}")    # Output: {'User_A', 'User_B', 'User_C'}

lucky_draw = {"Amit", "Neha", "Rahul", "Priya"}

# Pick a random winner from the pool
winner = lucky_draw.pop()

print(f"The winner is: {winner}")
print(f"Remaining pool: {lucky_draw}")