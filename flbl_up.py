# 1. Positional Unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4] (captures everything in between)
print(last)    # Output: 5


# 2. Merging Dictionaries with **
defaults = {"theme": "dark", "notifications": True}
user_settings = {"notifications": False, "font_size": 14}

# Merge: right side overrides left side for duplicate keys
config = {**defaults, **user_settings}

print(config)
# Output: {'theme': 'dark', 'notifications': False, 'font_size': 14}