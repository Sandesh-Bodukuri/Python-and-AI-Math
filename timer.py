import time

def my_timer(func):
    """
    Decorator function that measures execution time of any function it wraps.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Run the original function and save its result
        result = func(*args, **kwargs)
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"[{func.__name__}] finished in {elapsed:.4f} seconds.")
        return result
        
    return wrapper


# Usage: Apply the decorator using the '@' symbol above any function


@my_timer
def process_data(items: list[int]):
    """Simulates a heavy calculation task."""
    time.sleep(0.5)  # Simulate processing delay
    return [x * 2 for x in items]


# Calling the function as normal—the decorator transparently runs around it!
output = process_data([1, 2, 3, 4, 5])
print(f"Result: {output}")