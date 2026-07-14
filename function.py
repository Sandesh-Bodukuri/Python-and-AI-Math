# 1. Defining the Function (Using parameters: usernames and target_id)
def verify_system_access(active_users, check_id):
    """
    Accepts a set of active users and a single target ID.
    Returns a status message and boolean access token.
    """
    # Defensive logic check
    if check_id in active_users:
        return f"Access Granted to key record: {check_id}", True
    else:
        return f"🚨 SECURITY WARNING: Access Denied for {check_id}", False


# The Main Execution Code Space
# Custom system sets
verified_employees = {"EMP_01", "EMP_02", "EMP_03"}

# Calling the function multiple times with completely different arguments
verdict_1, status_1 = verify_system_access(verified_employees, "EMP_02")
print(f"Test Run A -> {verdict_1} (Status: {status_1})")

verdict_2, status_2 = verify_system_access(verified_employees, "EMP_99")
print(f"Test Run B -> {verdict_2} (Status: {status_2})")