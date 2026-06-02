total_bill= input("Enter the total restaurant bill amount:")
total_bill = float(total_bill)
n = input("Enter number of persons splitting the bill:")
n = int(n)
tip = input("Enter the tip percentage you want to give:")
tip = float(tip)

tip_amount = total_bill * (tip / 100)
grand_total = total_bill + tip_amount
amount_per_person = grand_total / n
print(f"The amount to be paid by each person : {amount_per_person:.2f}")

