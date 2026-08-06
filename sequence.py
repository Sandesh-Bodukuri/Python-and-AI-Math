import itertools
# 1. itertools.chain(): Combine Iterables Cleanly

active_users = ["Alice", "Bob"]
new_users = ["Charlie", "Diana"]

# Avoids allocating a new list like `active_users + new_users`
for user in itertools.chain(active_users, new_users):
    print(f"User: {user}")

# 2. itertools.zip_longest(): Zip with Missing Value Fill

headers = ["Name", "Age", "Role"]
data = ["Alice", 30]  # Missing 'Role'

# Standard zip() stops at shortest; zip_longest pads missing values
profile = dict(itertools.zip_longest(headers, data, fillvalue="N/A"))
print(f"Profile: {profile}")
# Output: Profile: {'Name': 'Alice', 'Age': 30, 'Role': 'N/A'}

# 3. itertools.groupby(): Group Consecutive Matching Items

transactions = [
    {"type": "income", "amount": 100},
    {"type": "income", "amount": 200},
    {"type": "expense", "amount": 50},
    {"type": "expense", "amount": 20},
]

# Note: Data MUST be sorted by key field prior to grouping
for key, group in itertools.groupby(transactions, key=lambda x: x["type"]):
    total = sum(item["amount"] for item in group)
    print(f"Total {key}: ${total}")
