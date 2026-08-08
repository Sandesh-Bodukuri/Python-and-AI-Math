def process_user_data(file_path: str):
    print("1. Opening file connection...")
    
    try:
        # Should Keep ONLY the code that might raise the targeted exception inside 'try'
        file = open(file_path, "r")
        data = file.read()
        
    except FileNotFoundError:
        # Runs ONLY if the specific exception occurs
        print(f"Error: File '{file_path}' was not found.")
        
    else:
        # Runs ONLY if NO exceptions occurred in the 'try' block
        # Place safe downstream processing code here!
        word_count = len(data.split())
        print(f"Success! File processed. Word count: {word_count}")
        
    finally:
        # Runs ALWAYS (whether an exception occurred or not)
        # Ideal for safety cleanup operations
        print("2. Cleanup completed (Connection closed).")

# Usage Examples

# Case A: Success Path
process_user_data("existing_log.txt")

print("-" * 40)

# Case B: Failure Path
process_user_data("missing_file.txt")