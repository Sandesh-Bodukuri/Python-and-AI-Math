import sys

# 1. Standard Class (Uses __dict__)

class StandardPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


# 2. Optimized Class (Uses __slots__)

class SlottedPoint:
    # Explicitly whitelist the allowed attribute names
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# 3. Memory & Behavior Comparison

p_standard = StandardPoint(10.5, 20.5)
p_slotted = SlottedPoint(10.5, 20.5)

# Standard instances have a __dict__ that takes extra memory
print(f"Standard instance size: {sys.getsizeof(p_standard)} bytes (plus __dict__: {sys.getsizeof(p_standard.__dict__)} bytes)")
print(f"Slotted instance size:  {sys.getsizeof(p_slotted)} bytes (no __dict__)")

# Behavior difference: __slots__ restricts dynamic attribute creation
# p_slotted.z = 30.0  # Raises AttributeError: 'SlottedPoint' object has no attribute 'z'