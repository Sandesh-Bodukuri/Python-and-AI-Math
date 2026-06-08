principal = float(input("Enter the initial investment amount :"))
interest = float(input("Enter annual interest rate :"))
rate = interest/100

#calculatuing compund interest for 5,10,15 years
bal_5 = principal * (1+rate)**5
bal_10 = principal * (1+rate)**10
bal_15 = principal * (1+rate)**15

doubling_years = int(72//interest)


print("             FINANCIAL DASHBOARD             ")
print(f"Initial Investment principal:{principal:.2f}")
print(f"Annual Interest:{interest:.2f}")

print(f"Estimated balance(5 years) :{bal_5:.2f}")
print(f"Estimated balance (10 years) :{bal_10:.2f}")
print(f"Estimated balance (15 years) :{bal_15:.2f}")

print(f"Estimated years to double: {doubling_years}years")

if doubling_years % 2 != 0 :
    print("Doubling years are odd")
else :
    print("Doubling years are even")

