filename = "user_data.txt"

# 1. WRITING: Opens file, writes lines, and closes it automatically
with open(filename, "w") as file:
    file.write("User: Alice\n")
    file.write("Role: Developer\n")
    file.write("Status: Active\n")

# At this line, 'file' is officially closed and saved!


# 2. READING: Opens file, reads content, and cleans up after
with open(filename, "r") as file:
    lines = file.readlines()
    
print("--- Extracted Data ---")
for line in lines:
    print(line.strip())

# The file is safely closed here too—no manual file.close() needed!