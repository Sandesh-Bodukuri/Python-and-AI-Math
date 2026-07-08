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


veg_pizza_toppings = {"Mushroom", "Paneer", "Onion"}
meat_lovers_toppings = {"Chicken", "Pepperoni", "Bacon"}

# Do they overlap?
print(veg_pizza_toppings.isdisjoint(meat_lovers_toppings))  # Output: True

primary_colors = {"Red", "Yellow", "Blue"}
all_colors = {"Red", "Yellow", "Blue", "Green", "Purple"}

# Using comparison symbols
print(primary_colors <= all_colors)  # Output: True
print(all_colors >= primary_colors)  # Output: True