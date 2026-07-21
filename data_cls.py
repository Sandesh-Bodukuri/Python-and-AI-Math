from dataclasses import dataclass

# 1. Add the @dataclass decorator
@dataclass
class User:
    # 2. Just list your variables with type hints!
    username: str
    email: str
    age: int
    is_active: bool = True  # Default value


# --- USING THE DATACLASS ---

# Python automatically created the __init__ method for you!
user1 = User(username="alex_dev", email="alex@email.com", age=25)

# Python automatically created a clean print representation!
print(user1)
# Output: User(username='alex_dev', email='alex@email.com', age=25, is_active=True)

# Access variables directly with dot notation
print(f"User Email: {user1.email}")