# Scope Lookup Hierarchy (LEGB)

site_name = "Global Site"  # Global scope

def outer_function():
    site_name = "Enclosing Site"  # Enclosing scope

    def inner_function():
        site_name = "Local Site"  # Local scope
        print(f"Inside inner: {site_name}")

    inner_function()
    print(f"Inside outer: {site_name}")

outer_function()
print(f"Top-level: {site_name}")


#nonlocal vs global
counter = 0  # Global variable

def update_counters():
    step = 10  # Enclosing variable

    def inner_worker():
        nonlocal step     # Binds to the enclosing 'step' variable
        global counter    # Binds to the module-level 'counter' variable

        step += 5
        counter += 1
        print(f"[Worker] step = {step}, counter = {counter}")

    inner_worker()
    print(f"[Outer] step after worker = {step}")

update_counters()
print(f"[Global] counter after run = {counter}")