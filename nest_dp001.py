# --- Simple Nested Data Structure ---
user_profile = {
    "username": "CodeNewbie",
    "subscription": ("Premium", 14.99),  # Tuple: (Plan Tier, Price)
    "favorite_genres": ["Sci-Fi", "Comedy", "Tech Docs"]  # List of items
}

# --- Parsing the Data ---

# 1. Parsing standard dictionary values
print(f"User: {user_profile['username']}")

# 2. Parsing the Tuple (Unpacking fixed values)
plan_name, price = user_profile["subscription"]
print(f"Plan: {plan_name} (${price}/month)")

# 3. Parsing the List (Looping through data elements)
print("Favorite Genres:")
for genre in user_profile["favorite_genres"]:
    print(f" - {genre}")