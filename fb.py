def calculate_invoice(price: float, qty: int = 1, tax_rate: float = 0.05, discount: float = 0.0):
    """Calculates final order total using smart defaults for quantity, tax, and discount."""
    
    subtotal = price * qty
    discounted_amount = subtotal - discount
    final_total = discounted_amount * (1 + tax_rate)
    
    return final_total


# --- 1. Basic Call (Uses all default values!) ---
# Only 'price' is required; qty becomes 1, tax becomes 5%, discount becomes $0
total_1 = calculate_invoice(50.0)
print(f"Standard Item (1 x $50): ${total_1:.2f}")


# --- 2. Overriding specific defaults with Keyword Arguments ---
# We explicitly set a discount, but leave tax_rate at its default 5%
total_2 = calculate_invoice(price=100.0, qty=2, discount=15.0)
print(f"Bulk Purchase (2 x $100 with $15 off): ${total_2:.2f}")


# --- 3. Passing arguments in ANY order via Keywords ---
# Because we name the parameters, order no longer matters!
total_3 = calculate_invoice(tax_rate=0.10, price=200.0, qty=1)
print(f"High-Tax Region (1 x $200 at 10% tax): ${total_3:.2f}")