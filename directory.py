# Open the Operating System toolbox
import os

print("=== SYSTEMS PATH DETECTIVE ===")

# 1. Ask your computer: "Where am I currently running this script?"
current_location = os.getcwd()  # getcwd = Get Current Working Directory
print(f"Current Folder Path: {current_location}")

# 2. Check if a specific file exists on your hard drive before opening it
target_file = "guestbook.txt"
file_exists = os.path.exists(target_file)

print(f"Checking for '{target_file}'...")
if file_exists:
    print("✅ File found! Safe to open and process.")
else:
    print("❌ File missing! We should create it first to avoid errors.")

print("==============================")