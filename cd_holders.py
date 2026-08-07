from dataclasses import dataclass, field

# 1. Defining a Data Class

@dataclass
class UserProfile:
    user_id: int
    username: str
    email: str
    is_active: bool = True  # Default argument
    tags: list[str] = field(default_factory=list)  # Safe default for mutable types

# 2. Auto-Generated Features in Action
# Automatically gets an __init__() constructor
user1 = UserProfile(user_id=101, username="alice", email="alice@example.com")
user2 = UserProfile(user_id=101, username="alice", email="alice@example.com")

# 1. Auto-generated clean string representation (__repr__)
print(user1)

# 2. Auto-generated value equality comparison (__eq__)
print(f"Are users equal? {user1 == user2}")
