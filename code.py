# 1. Mock Corporate Database
employees = {
    "EMP01": {"name": "Siddharth", "salary": 95000},
    "EMP02": {"name": "Kriti", "salary": 120000},
    "EMP03": {"name": "Varun", "salary": 48000}
}

print("=" * 45)
print("         CORPORATE PAYROLL SYSTEM          ")
print("==========================================")

# 2. Taxation Processing Loop (.items() unpacking)
for emp_id, info in employees.items():
    name = info["name"]
    salary = info["salary"]
    
    # 3. Graduated Tax Logic
    if salary > 100000:
        tax_rate = 0.30
    elif 50000 <= salary <= 100000:
        tax_rate = 0.20
    else:
        tax_rate = 0.10
        
    tax_deduction = salary * tax_rate
    
    # 4. Net Pay Calculation
    net_pay = salary - tax_deduction
    
    # 5. Dashboard Output (Formatted with :,.2f)
    print(f"[Advice Pay Stub for ID: {emp_id}]")
    print(f"  Employee Name      : {name}")
    print(f"  Gross Base Salary  : ${salary:,.2f}")
    print(f"  Tax Withholding ({int(tax_rate*100)}%): ${tax_deduction:,.2f}")
    print(f"  Net Take-Home Pay  : ${net_pay:,.2f}")
    print("-" * 42)

print("==========================================")