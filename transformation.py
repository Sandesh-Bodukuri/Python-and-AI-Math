# 1. List Comprehension: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Traditional loop replacement: filter evens and square them
squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Squared Evens: {squared_evens}")



# 2. Dictionary Comprehension: {key: value for item in iterable}

users = [("alice", "admin"), ("bob", "user"), ("charlie", "admin")]

# Map user names to uppercase roles
user_role_map = {name: role.upper() for name, role in users}
print(f"User Roles: {user_role_map}")



# 3. Set Comprehension: {expression for item in iterable}

tags = ["Python", "python", "DJANGO", "Django", "code"]

# Normalize and deduplicate tags instantly
unique_tags = {tag.lower() for tag in tags}
print(f"Unique Tags: {unique_tags}")
