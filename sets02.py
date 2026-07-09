# Raw log data containing duplicate logins throughout the day
mobile_logs = ["user_101", "user_102", "user_101", "user_103", "user_105", "user_102"]
web_logs = ["user_103", "user_104", "user_105", "user_106", "user_103"]

# Step 1: Convert raw lists to sets to automatically remove duplicates
mobile_users = set(mobile_logs)
web_users = set(web_logs)

print(f"Unique Mobile Users : {mobile_users}")
print(f"Unique Web Users    : {web_users}")
print("-" * 55)

# Task 1: Find all unique users across EITHER platform (Union)
# Operator shortcut: mobile_users | web_users
all_active_users = mobile_users.union(web_users)
print(f"1. Total Unique Platform Users:\n   {all_active_users}")

# Task 2: Find users who logged into BOTH platforms (Intersection)
# Operator shortcut: mobile_users & web_users
dual_platform_users = mobile_users.intersection(web_users)
print(f"\n2. Highly Active Users (Both Mobile & Web):\n   {dual_platform_users}")

# Task 3: Find users who ONLY used the mobile app (Difference)
# Operator shortcut: mobile_users - web_users
only_mobile_users = mobile_users.difference(web_users)
print(f"\n3. Users who exclusively used Mobile:\n   {only_mobile_users}")