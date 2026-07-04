# --- 1. Creating Sets ---
# Note: Sets use curly braces {}, just like dictionaries, but without key-value pairs.
ai_club = {"Amit", "Neha", "Rahul", "Srinivas", "Neha"}  # "Neha" is added twice intentionally
web_dev_club = {"Rahul", "Priya", "Janardhan", "Srinivas"}

# Notice how the duplicate "Neha" is automatically removed when we print it
print(f"AI Club Members: {ai_club}") 
print(f"Web Dev Club Members: {web_dev_club}")

print("-" * 50)

# --- 2. Common Set Operations ---

# A. INTERSECTION (&): Who is in BOTH clubs?
# Finds only the elements that exist in both sets
both_clubs = ai_club.intersection(web_dev_club)
# Alternative syntax: both_clubs = ai_club & web_dev_club
print(f"Members in BOTH clubs: {both_clubs}")


# B. UNION (|): Who is in AT LEAST one club?
# Combines all members from both sets, eliminating any duplicates
all_students = ai_club.union(web_dev_club)
# Alternative syntax: all_students = ai_club | web_dev_club
print(f"Total unique students across all clubs: {all_students}")


# C. DIFFERENCE (-): Who is ONLY in the AI Club?
# Takes the AI club and removes anyone who is also in the Web Dev club
only_ai = ai_club.difference(web_dev_club)
# Alternative syntax: only_ai = ai_club - web_dev_club
print(f"Students ONLY in the AI Club: {only_ai}")


# D. SYMMETRIC DIFFERENCE (^): Who is in one club but NOT both?
# Grabs students who haven't double-booked themselves
not_shared = ai_club.symmetric_difference(web_dev_club)
# Alternative syntax: not_shared = ai_club ^ web_dev_club
print(f"Students in only one specific club: {not_shared}")

print("-" * 50)

# --- 3. Modifying a Set ---
# Elements can be added or removed dynamically
ai_club.add("Kiran")       # Adds an item
ai_club.remove("Amit")     # Removes an item

print(f"Updated AI Club: {ai_club}")