file_name = "guestbook.txt"

# 1. Writing to a File ("a" mode stands for APPEND)
# If the file doesn't exist, Python will automatically create it!
visitor_name = input("Enter your name to sign the guestbook: ").strip()

with open(file_name, "a") as file:
    # We add a newline character (\n) so each guest gets their own line
    file.write(f"{visitor_name}\n")
    
print("📝 Name saved permanently to guestbook.txt!\n")


# 2. Reading from a File ("r" mode stands for READ)
print("=== LIVE VISITOR LOG ===")
try:
    with open(file_name, "r") as file:
        # Read all lines from the text file into a Python list
        guests = file.readlines()
        
        # Loop through and print each guest cleanly
        for index, guest in enumerate(guests, start=1):
            # .strip() removes the trailing newline character (\n) from the file
            print(f"Guest #{index}: {guest.strip()}")
            
except FileNotFoundError:
    print("No visitors have signed the guestbook yet!")

print("========================")