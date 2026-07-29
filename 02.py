def handle_command(command: str):
    """Executes different logic based on user input."""
    
    # Standardize string input
    match command.strip().lower():
        case "start" | "go":
            print("System starting up...")
            
        case "stop" | "pause":
            print("System paused.")
            
        case "quit" | "exit":
            print("Exiting application. Goodbye!")
            
        case _:
            # The underscore '_' acts as the wild-card default case (like 'else')
            print(f"Unknown command: '{command}'. Please try again.")


# ---------------------------------------------------------------------
# Usage Examples
# ---------------------------------------------------------------------

handle_command("START")   # Matches "start" | "go"
handle_command("pause")   # Matches "stop" | "pause"
handle_command("restart") # Matches default wildcard case _

# Output:
# System starting up...
# System paused.
# Unknown command: 'restart'. Please try again.