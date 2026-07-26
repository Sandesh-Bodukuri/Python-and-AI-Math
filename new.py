def safe_divide(numerator: float, denominator_input: str):
    """Attempts to convert input and divide two numbers safely."""
    try:
        # Convert string input to float and perform division
        denominator = float(denominator_input)
        result = numerator / denominator

    except ValueError:
        # Triggers if float() conversion fails (e.g., user typed "abc")
        print("Error: Please enter a valid numeric string, not text!")

    except ZeroDivisionError:
        # Triggers if the denominator is 0
        print("Error: You cannot divide a number by zero!")

    else:
        # Runs ONLY if NO exceptions occurred in the try block
        print(f"Success! Result: {numerator} / {denominator} = {result}")

    finally:
        # Runs EVERY single time, regardless of whether there was an error or not
        print("--- Calculation attempt finished ---\n")


# ---------------------------------------------------------------------
# Testing the function with different inputs
# ---------------------------------------------------------------------

safe_divide(10, "2")    # Case 1: Valid input (Triggers 'else')
safe_divide(10, "0")    # Case 2: Division by zero (Triggers ZeroDivisionError)
safe_divide(10, "hello")# Case 3: Invalid text input (Triggers ValueError)