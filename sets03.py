# 1. Mock Database
employees = {
    "EMP01": {"name": "Siddharth", "salary": 95000},
    "EMP02": {"name": "Kriti", "salary": 120000},
    "EMP03": {"name": "Varun", "salary": 48000}
}

# 2. Bracket Lookup Configuration (Threshold, Tax Rate)
# MUST be ordered from highest threshold down to lowest
TAX_BRACKETS = (
    (100000, 0.30),
    (50000,  0.20),
    (0,      0.10)
)

print("============ MINI PAYROLL SYSTEM ============")

# 3. Compact Processing Loop
for emp_id, info in employees.items():
    sal = info["salary"]
    
    # Efficient Lookup: Find the first threshold the salary beats
    rate = next(rate for limit, rate in TAX_BRACKETS if sal > limit)
    
    # Direct Calculations
    tax = sal * rate
    net = sal - tax
    
    # 4. Dashboard Output
    print(f"{info['name']} ({emp_id}) -> Gross: ${sal:,.0f} | Tax ({int(rate*100)}%): ${tax:,.0f} | Net: ${net:,.0f}")

print("=============================================")